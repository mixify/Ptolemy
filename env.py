from gui import Macro
def env():

    macros = []
    env.observation_space.shape
    env.action_space.n
    pre_score = 0

    def step(action):

        if(action>0):#do nothing
            action.runMacro(macros[action])

        if(pre_score < score):
            reward = 1
        elif(pre_score == score):
            reward = 0
        else:
            reward = -1
        reward = 0 # get from ocr

        next_state = 0#Capture
        return (next_state, reward, done)

    def reset():


