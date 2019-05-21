from interrupt import Macro as mc
import image_matching as im
class env():

    def __init__(self):
        self.actions = []
        self.actions.append(0)
        self.pre_score = 0
        '''
        Test codes~~~~~~
        this should be changed to variables version
        def __init__(self,observations which is cv image matched data,actions which is macros):
        '''
        ### observation_space
        self.observation_space = im.get_shape()
        self.time_step = 0;
        self.best_time_step = 0;
        self.is_alive = True
        ### actions

        macros = []
        macro1 = mc.Macro()
        # new_macro.setDelay(3)
        macro1.setKeyPress('space')
        macros.append(macro1)

        # new_macro.setDelay(3)
        # macros.append(macro2)



        '''
        test codes
        end here
        '''
        self.actions.append(macro1)

    def set_actions(self, macros):
        '''
        set actions
        for test this is temporary func
        '''
        self.actions = macros

    def step(self, action_num):


        ### should really think about how game over is recongnized
        # self.is_alive, next_state = get_state()#Capture
        ### should really think about how game over is recongnized


        self.time_step+=1
        print(action_num)
        if(action_num>0):#do nothing if no op
            self.actions[action_num].runMacro()

        score = 0
        '''
        score = get_score_from_ocr
        '''
        self.best_time_step = max(self.best_time_step,self.time_step)
        if(self.time_step>self.best_time_step):
            reward = 1
        elif(self.is_alive==False):
            reward = -3
        else:
            reward = 0
        # if(pre_score < score):
        #     reward = 1
        # elif(pre_score == score):
        #     reward = 0
        # else:
        #     reward = -1

        # pre_score = score;

        reward = 0 # get from ocr

        done, next_state = im.get_state()#Capture
        return (next_state, reward, done, 0)

    def reset(self):
#         self.pre_score = 0
        self.actions[1].runMacro()
        self.actions[1].runMacro()
        self.time_step = 0
        self.is_alive = True
        _, state = im.get_state()
        return state

# e = env()
# e.set_actions('a')
# e.actions[1].runMacro()
