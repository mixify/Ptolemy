import mouse
import keyboard

class EventHook:
    def __init__(self):
        self.x_pos = None
        self.y_pos = None
        self.key = None

    def MouseEvent(self, event):
        if isinstance(event, mouse.MoveEvent):
            self.x_pos = event.x
            self.y_pos = event.y

    def KeyboardEvent(self, event):
        self.key = event.name
    
    def startMouseHook(self):
        mouse.hook(self.MouseEvent)

    def stopMouseHook(self):
        mouse.unhook_all()

    def startKeyboardHook(self):
        keyboard.on_press(self.KeyboardEvent)
    
    def stopKeyboardHook(self):
        keyboard.unhook_all()

if __name__ == '__main__':
    mh = EventHook()
    mh.startMouseHook()
    mh.startKeyboardHook()
    keyboard.wait('esc')
    mh.stopMouseHook()
    mh.stopKeyboardHook()