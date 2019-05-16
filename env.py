from interrupt import Macro as mc
class env():

    macros = [0]
    pre_score = 0

    def __init__(self):
        macros = [0]

    def set_actions(self,macro):
        '''
        set actions
        for test this is temporary func
        '''
        new_macro = mc.Macro()
        new_macro.setKeyPress('space')
        self.macros.append(new_macro)

    def step(self,action):

        if(action>0):#do nothing if no op
            runMacro(macros[action])

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
        print('reset~~~')

e = env()
e.set_actions('a')
e.macros[1].runMacro()
