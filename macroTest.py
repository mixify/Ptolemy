import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
import win32api
import pyautogui

class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.x = QLineEdit()
        self.t_le = QLineEdit()
        self.start_btn = QPushButton('Start', self)
        self.timer = QTimer()

        self.initUI()

    def initUI(self):

        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(QLabel('String: '))
        hbox1.addWidget(self.x)
        hbox1.addStretch(1)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(QLabel('Delay: '))
        hbox2.addWidget(self.t_le)
        hbox2.addStretch(1)

        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(self.start_btn)
        hbox3.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)

        self.setLayout(vbox)

        self.start_btn.clicked.connect(self.start_btn_click)

        self.setWindowTitle('Ptolemy')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def start_btn_click(self):

        delay = int(self.t_le.text())
        self.timer.start(delay*1000)
        self.timer.timeout.connect(self.keyboard_click)

    def keyboard_click(self):

        pyautogui.typewrite(self.x.text()+' ', interval=0.25)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())