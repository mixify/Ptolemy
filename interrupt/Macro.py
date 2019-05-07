import keyboard
import mouse
import numpy as np
import time

class Macro:
    def __init__(self):
        self.event_data = []
        self.last_time = None

    def setRecordEvent(self, event):
        delay = None
        
        if not isinstance(event, mouse.WheelEvent):
            if self.last_time is None:
                delay = 0
            else:
                delay = event.time - self.last_time
            self.last_time = event.time

            if isinstance(event, keyboard.KeyboardEvent):
                self.addEventData(1, event.event_type, event.name, delay)

            elif isinstance(event, mouse.ButtonEvent):
                self.addEventData(2, event.event_type, event.button, delay)

            elif isinstance(event, mouse.MoveEvent):
                self.addEventData(3, event.x, event.y, delay)
        
    def loadScript(self, fname):
        self.event_data = np.genfromtxt(fname, encoding='ascii', dtype=None, delimiter='/')
    
    def saveScript(self, fname):
        f = open(fname,'wt', encoding='UTF-8')
        text=''
        for e in self.event_data:
            text+='/'.join(str(s) for s in e)
            text+='\n'
        f.write(text)
        f.close()

    def startRecord(self, since='esc', include_keyboard=True, include_mouse=True):
        self.clearEventData()
        keyboard.wait(since)
        if include_keyboard:
            keyboard.hook(self.setRecordEvent)
        if include_mouse:
            mouse.hook(self.setRecordEvent)

    def stopRecord(self, until='esc'):
        keyboard.wait(until)
        keyboard.unhook_all()
        mouse.unhook_all()
        del(self.event_data[0])
        del(self.event_data[-1])

    def setKeyPress(self, event_name):
        self.setKeyDown(event_name)
        self.setKeyUp(event_name)
    
    def setKeyDown(self, event_name):
        self.addEventData(1, 'down', event_name, 0)

    def setKeyUp(self, event_name):
        self.addEventData(1, 'up', event_name, 0)

    def setMouseClick(self, event_name):
        self.setMouseDown(event_name)
        self.setMouseUp(event_name)

    def setMouseDown(self, event_name):
        self.addEventData(2, 'down', event_name, 0)

    def setMouseUp(self, event_name):
        self.addEventData(2, 'up', event_name, 0)

    def setMouseMove(self, x_pos, y_pos, duration=0):
        self.addEventData(3, x_pos, y_pos, duration)

    def setMouseDrag(self, s_x_pos, s_y_pos, e_x_pos, e_y_pos, duration=0.1):
        start_pos = [s_x_pos, s_y_pos]
        end_pos = [e_x_pos, e_y_pos]
        self.addEventData(4, start_pos, end_pos, duration)

    def setDelay(self, delay):
        self.addEventData(0, 0, 0, delay)

    def clearEventData(self):
        self.event_data.clear()
        self.last_time = None

    def addEventData(self, option, event_type, event_name, delay):
        temp = []
        temp.append(option)
        temp.append(event_type)
        temp.append(event_name)
        temp.append(delay)
        self.event_data.append(temp)

    def runMacro(self):
        for (option, event_type, event_name, delay) in self.event_data:
            time.sleep(delay)
            
            if option == 1: # keyboard click
                key = event_name
                keyboard.press(key) if event_type == 'down' else keyboard.release(key)
            elif option == 2: # mouse click
                if event_type == 'up':
                    mouse.release(event_name)
                else:
                    mouse.press(event_name)
            elif option == 3: # mouse move
                mouse.move(int(event_type), int(event_name), True, delay)
            elif option == 4: # mouse drag
                start_pos = list(event_type)
                end_pos = list(event_name)
                mouse.drag(start_pos[0], start_pos[1], end_pos[0], end_pos[1], True, delay)
                

if __name__ == '__main__':
    macro = Macro()
    macro.startRecord()
    macro.stopRecord()
    macro.saveScript('keylog.txt')
    '''
    macro.setKeyDown('shift')
    macro.setDelay(0.01)
    macro.setKeyPress('a')
    macro.setDelay(1.212)
    macro.setKeyPress('b')
    macro.setDelay(0.01)
    macro.setKeyUp('shift')
    macro.setDelay(1)
    macro.setKeyPress('b')
    macro.setDelay(1.35543)
    macro.setKeyPress('c')
    macro.setDelay(1.60409)
    macro.setKeyPress('d')
    macro.saveScript('keylog.txt')
    
    macro.setDelay(1)
    macro.setMouseDrag(0, 0, 200, 200)
    macro.saveScript('keylog.txt')
    macro.runMacro()
    '''