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
        observation_space = im.get_state()
        ### actions

        macros = []
        macro1 = mc.Macro()
        # new_macro.setDelay(3)
        macro1.setKeyPress('space')
        macros.append(macro1)

        macro2 = mc.Macro()
        # new_macro.setDelay(3)
        macro2.setKeyPress('down')
        macros.append(macro2)

<<<<<<< HEAD


        '''
        test codes
        end here
        '''
        self.actions = macros

=======


        '''
        test codes
        end here
        '''
        self.actions = macros

>>>>>>> 4c60ae30343ead2d7bbc950351335f4098f57906
    def set_actions(self,macros):
        '''
        set actions
        for test this is temporary func
        '''
<<<<<<< HEAD
<<<<<<< HEAD
        new_macro = mc.Macro()
        new_macro.setDelay(4)
        new_macro.setKeyPress('space')
      
        self.macros.append(new_macro)


    def step(self,action):
=======
        self.actions = macros

    def step(self,action_num):
>>>>>>> 4c60ae30343ead2d7bbc950351335f4098f57906
=======
        self.actions = macros

    def step(self,action_num):
>>>>>>> 4c60ae30343ead2d7bbc950351335f4098f57906


        ### should really think about how game over is recongnized
        # done, next_state = get_state()#Capture
        ### should really think about how game over is recongnized

        if(action_num>0):#do nothing if no op
            runMacro(actions[action_num])

        score = 0
        '''
        score = get_score_from_ocr
        '''
        if(pre_score < score):
            reward = 1
        elif(pre_score == score):
            reward = 0
        else:
            reward = -1

        pre_score = score;

        reward = 0 # get from ocr

        done, next_state = get_state()#Capture
        return (next_state, reward, done)

    def reset(self):
        time_step = 0
        print('reset~~~')

# e = env()
# e.set_actions('a')
# e.actions[1].runMacro()
