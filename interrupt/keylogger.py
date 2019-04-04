import keyboard
import mouse

class KeyLogger:

    def __init__(self):
        self.saveKey = []
    
    def OnKeyboardEvent(self, event):
        print('EventType:', event.event_type)
        print('EventTime:', event.time)
        print('EventName:', event.name)
        print('--------------------------')

        self.saveKey.append('1 ')
        self.saveKey.append(event.event_type)
        self.saveKey.append(' ')
        self.saveKey.append(event.name)
        self.saveKey.append(' ')
        self.saveKey.append(event.time)
        self.saveKey.append('\n')

        return True

    def OnMouseEvent(self, event):

        if isinstance(event, mouse.ButtonEvent):
            self.saveKey.append('2 ')
            self.saveKey.append(event.event_type)
            self.saveKey.append(' ')
            self.saveKey.append(event.button)
            self.saveKey.append(' ')
            self.saveKey.append(event.time)
            self.saveKey.append('\n')

        elif isinstance(event, mouse.MoveEvent):
            self.saveKey.append('3 ')
            self.saveKey.append(event.x)
            self.saveKey.append(' ')
            self.saveKey.append(event.y)
            self.saveKey.append(' ')
            self.saveKey.append(event.time)
            self.saveKey.append('\n')
 
        return True

    def startRecord(self):
        keyboard.hook(self.OnKeyboardEvent)
        mouse.hook(self.OnMouseEvent)

    def stopRecord(self):
        keyboard.unhook_all()
        mouse.unhook_all()

    def saveKeyLog(self):
        f = open("keylog.txt",'wt', encoding='UTF-8')
        text = ''
        text="".join(str(s) for s in self.saveKey)
        f.write(text)
        f.close()

if __name__ == '__main__':

    keylogger = KeyLogger()
    keylogger.startRecord()
    keyboard.wait('esc')
    keylogger.stopRecord()
    keylogger.saveKeyLog()