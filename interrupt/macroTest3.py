import sys
import pyautogui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import macro
import time

class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.m = macro.Macro()
        self.open_btn = QPushButton('Open Script')

        self.n_le = QLineEdit()
        self.t_le = QLineEdit()
        self.start_btn = QPushButton('Start')
        self.fname = []
        self.vbox = QVBoxLayout()
        self.initUI()

    def initUI(self):

        hbox_nt = QHBoxLayout()
        hbox_nt.addWidget(QLabel('횟수: '))
        hbox_nt.addWidget(self.n_le)
        hbox_nt.addWidget(QLabel('딜레이: '))
        hbox_nt.addWidget(self.t_le)

        self.vbox.addWidget(self.open_btn)
        self.vbox.addStretch(1)

        self.vbox.addLayout(hbox_nt)
        self.vbox.addStretch(1)

        self.vbox.addWidget(self.start_btn)
        self.setLayout(self.vbox)

        self.open_btn.clicked.connect(self.show_dialog)
        self.start_btn.clicked.connect(self.start_btn_clicked)

        self.setWindowTitle('Ptolemy')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def show_dialog(self):

        fname = QFileDialog.getOpenFileName(self, 'Open file', './')

        if fname[0]:
            self.m.readScripts(fname[0])
            
    def start_btn_clicked(self):
        n = int(self.n_le.text())
        t = float(self.t_le.text())

        time.sleep(t)
        for i in range(n):
            self.m.runMacro()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())