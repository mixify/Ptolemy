import keyboard
import mouse
import numpy as np
import time

class Macro:
    def __init__(self):
        self.loaded_data = []

    def readScripts(self, fname):
        self.loaded_data = np.genfromtxt(fname, encoding='ascii', names=('option', 'event_type', 'event_name', 'event_time'), dtype=None)
        print(self.loaded_data)

    def runMacro(self):
        last_time = None
        for (option, event_type, event_name, event_time) in self.loaded_data:
            if last_time is not None:
                time.sleep(event_time - last_time)
            last_time = event_time

            if option == 1:
                key = event_name
                keyboard.press(key) if event_type == 'down' else keyboard.release(key)
            elif option == 2:
                if event_type == 'up':
                    mouse.release(event_name)
                else:
                    mouse.press(event_name)
            elif option == 3:
                mouse.move(int(event_type), int(event_name))