import math, random

import signal
import sys

import numpy as np

import torch
import torch.nn as nn
import torch.optim as optim
import torch.autograd as autograd
import torch.nn.functional as F

from common.layers import NoisyLinear
from common.replay_buffer import ReplayBuffer

from datetime import timedelta
import time

import env
env = env.env()

original_sigint = signal.getsignal(signal.SIGINT)

USE_CUDA = torch.cuda.is_available()
Variable = lambda *args, **kwargs: autograd.Variable(*args, **kwargs).cuda() if USE_CUDA else autograd.Variable(*args, **kwargs)

def update_target(current_model, target_model):
    target_model.load_state_dict(current_model.state_dict())

#update_target(current_model, target_model)

def projection_distribution(next_state, rewards, dones):
    batch_size  = next_state.size(0)

    delta_z = float(Vmax - Vmin) / (num_atoms - 1)
    support = torch.linspace(Vmin, Vmax, num_atoms)

    next_dist   = target_model(next_state).data.cpu() * support
    next_action = next_dist.sum(2).max(1)[1]
    next_action = next_action.unsqueeze(1).unsqueeze(1).expand(next_dist.size(0), 1, next_dist.size(2))
    next_dist   = next_dist.gather(1, next_action).squeeze(1)

    rewards = rewards.unsqueeze(1).expand_as(next_dist)
    dones   = dones.unsqueeze(1).expand_as(next_dist)
    support = support.unsqueeze(0).expand_as(next_dist)

    Tz = rewards + (1 - dones) * 0.99 * support
    Tz = Tz.clamp(min=Vmin, max=Vmax)
    b  = (Tz - Vmin) / delta_z
    l  = b.floor().long()
    u  = b.ceil().long()

    offset = torch.linspace(0, (batch_size - 1) * num_atoms, batch_size).long()\
                    .unsqueeze(1).expand(batch_size, num_atoms)

    proj_dist = torch.zeros(next_dist.size())
    proj_dist.view(-1).index_add_(0, (l + offset).view(-1), (next_dist * (u.float() - b)).view(-1))
    proj_dist.view(-1).index_add_(0, (u + offset).view(-1), (next_dist * (b - l.float())).view(-1))

    return proj_dist


def compute_td_loss(batch_size):
    state, action, reward, next_state, done = replay_buffer.sample(batch_size)

    state      = Variable(torch.FloatTensor(np.float32(state)))
    next_state = Variable(torch.FloatTensor(np.float32(next_state)), volatile=True)
    action     = Variable(torch.LongTensor(action))
    reward     = torch.FloatTensor(reward)
    done       = torch.FloatTensor(np.float32(done))

    proj_dist = projection_distribution(next_state, reward, done)

    dist = current_model(state)
    action = action.unsqueeze(1).unsqueeze(1).expand(batch_size, 1, num_atoms)
    dist = dist.gather(1, action).squeeze(1)
    dist.data.clamp_(0.01, 0.99)
    loss = -(Variable(proj_dist) * dist.log()).sum(1)
    loss  = loss.mean()

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    current_model.reset_noise()
    target_model.reset_noise()

    return loss


class RainbowCnnDQN(nn.Module):
    def __init__(self, input_shape, num_actions, num_atoms, Vmin, Vmax):
        super(RainbowCnnDQN, self).__init__()

        self.input_shape   = input_shape
        self.num_actions  = num_actions
        self.num_atoms    = num_atoms
        self.Vmin         = Vmin
        self.Vmax         = Vmax

        self.features = nn.Sequential(
            nn.Conv2d(input_shape[0], 32, kernel_size=4, stride=4),
            nn.ReLU(),
            nn.Conv2d(32, 64, kernel_size=1, stride=2),
            nn.ReLU(),
            nn.Conv2d(64, 64, kernel_size=1, stride=1),
            nn.ReLU()
        )

        self.noisy_value1 = NoisyLinear(self.feature_size(), 512, use_cuda=USE_CUDA)
        self.noisy_value2 = NoisyLinear(512, self.num_atoms, use_cuda=USE_CUDA)

        self.noisy_advantage1 = NoisyLinear(self.feature_size(), 512, use_cuda=USE_CUDA)
        self.noisy_advantage2 = NoisyLinear(512, self.num_atoms * self.num_actions, use_cuda=USE_CUDA)

    def forward(self, x):
        batch_size = x.size(0)

        x = x / 255.
        x = self.features(x)
        x = x.view(batch_size, -1)

        value = F.relu(self.noisy_value1(x))
        value = self.noisy_value2(value)

        advantage = F.relu(self.noisy_advantage1(x))
        advantage = self.noisy_advantage2(advantage)

        value     = value.view(batch_size, 1, self.num_atoms)
        advantage = advantage.view(batch_size, self.num_actions, self.num_atoms)

        x = value + advantage - advantage.mean(1, keepdim=True)
        x = F.softmax(x.view(-1, self.num_atoms)).view(-1, self.num_actions, self.num_atoms)

        return x

    def reset_noise(self):
        self.noisy_value1.reset_noise()
        self.noisy_value2.reset_noise()
        self.noisy_advantage1.reset_noise()
        self.noisy_advantage2.reset_noise()

    def feature_size(self):
        return self.features(autograd.Variable(torch.zeros(1, *self.input_shape))).view(1, -1).size(1)

    def act(self, state):
        state = Variable(torch.FloatTensor(np.float32(state)).unsqueeze(0), volatile=True)
        dist = self.forward(state).data.cpu()
#        print(dist)
        dist = dist * torch.linspace(self.Vmin, self.Vmax, self.num_atoms)
        action = dist.sum(2).max(1)[1].numpy()[0]
        return action

num_atoms = 51
Vmin = -10
Vmax = 10

current_model = RainbowCnnDQN(env.observation_space, len(env.actions), num_atoms, Vmin, Vmax)
target_model  = RainbowCnnDQN(env.observation_space, len(env.actions), num_atoms, Vmin, Vmax)

if USE_CUDA:
    current_model = current_model.cuda()
    target_model  = target_model.cuda()

optimizer = optim.Adam(current_model.parameters(), lr=0.0001)
update_target(current_model, target_model)

replay_initial = 10000
replay_buffer  = ReplayBuffer(100000)

num_frames = 10000000
batch_size = 32
gamma      = 0.99

losses = []
all_rewards = []
episode_reward = 0

state = env.reset()

start = time.time()

original_sigint = signal.getsignal(signal.SIGINT)

def print_info():
    print(frame_idx)

def ctrlc_handler(signum, frame):
    signal.signal(signal.SIGINT, original_sigint)
    try:
        while(1):
            ans = input('\nPaused learning\npress (i) to see input\npress (y) to quit\npress (r) to resume\n:').lower()
            if(ans.startswith('y')):
                sys.exit()
            elif(ans.startswith('i')):
                print_info()
            elif(ans.startswith('r')):
                break

    except KeyboardInterrupt:
        print('I\'m quiting really')
        sys.exit()
    signal.signal(signal.SIGINT, ctrlc_handler)

signal.signal(signal.SIGINT, ctrlc_handler)


for frame_idx in range(1, num_frames + 1):
    action = current_model.act(state)
    #print(env.actions)

    print('action = ',action)
    next_state, reward, done, _ = env.step(action)
    if(frame_idx < 100):
        reward = 0
    print('reward :',reward)
    replay_buffer.push(state, action, reward, next_state, done)

    state = next_state
    episode_reward += reward

    if done:
        state = env.reset()
        all_rewards.append(episode_reward)
        episode_reward = 0

    if len(replay_buffer) > replay_initial:
        loss = compute_td_loss(batch_size)
        losses.append(loss.data)

    print(state[:,:,0].T)
    print('')

    if frame_idx % 10000 == 0:
        check_point = time.time()
        elapsed = check_point - start
        PATH = 'rainbow_dqn_neural'+str(timedelta(seconds=elapsed).replace(':','_'))
        torch.save(current_model.state_dict(),PATH)

    if frame_idx % 1000 == 0:
        update_target(current_model, target_model)
