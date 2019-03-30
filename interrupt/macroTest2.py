import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
import win32api
import pyautogui
import pyHook
import pyHookKeyLogger as KL

class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.keylogger = KL.KeyLogger()
        self.hm = pyHook.HookManager()
        self.hm.KeyDown = self.keylogger.OnKeyDownEvent
        self.hm.KeyUp = self.keylogger.OnKeyUpEvent

        self.start_btn = QPushButton('Start', self)
        self.stop_btn = QPushButton('Stop', self)
        self.initUI()

    def initUI(self):

        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(self.start_btn)
        hbox1.addStretch(1)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(self.stop_btn)
        hbox2.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)

        self.setLayout(vbox)

        self.start_btn.clicked.connect(self.start_btn_click)
        self.stop_btn.clicked.connect(self.stop_btn_click)

        self.setWindowTitle('Ptolemy')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def start_btn_click(self):
        self.hm.HookKeyboard()

    def stop_btn_click(self):

        self.keylogger.saveKeyLog()
        self.hm.UnhookKeyboard()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())