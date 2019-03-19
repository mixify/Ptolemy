
# coding: utf-8

# In[ ]:


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QAction, qApp
from PyQt5.QtGui import QFont,QIcon
from tkinter import *
import tkinter.messagebox

class MyApp:

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        
#        menu_bar = self.menuBar()
        
        
        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

 #       self.statusBar()

        btn1 = QPushButton('녹화',self)
        btn2 = QPushButton('시작',self)
        btn3 = QPushButton('중지',self)
        
        hbox = QHBoxLayout()
        hbox.addStretch(10)
        hbox.addWidget(btn1)
        hbox.addStretch(10)
        hbox.addWidget(btn2)
        hbox.addStretch(10)
        hbox.addWidget(btn3)
        hbox.addStretch(10)

        vbox = QVBoxLayout()
        vbox.addStretch(9)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        btn1.clicked.connect(self.print_btn1)
#        btn2.clicked.connect(self.print_btn2)
 #       btn3.clicked.connect(self.print_btn3)

        self.setLayout(vbox)
        self.setWindowTitle('Ptolemy')
        self.setGeometry(500, 500, 500, 500)
        self.show()

    def print_btn1(self):
        tkinter.messagebox.showinfo("tlqkf","tlqkf")
 #   def print_btn2(self):
        
#    def print_btn3(self):
        

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

