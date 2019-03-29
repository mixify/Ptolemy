
# coding: utf-8
"""
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import *
import tkinter.messagebox

class MyApp:

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        
        menu_bar = self.menuBar()
        
        
        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

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

    ## 키로그 따오는거 시작.
    def print_btn1(self):
        tkinter.messagebox.showinfo("tlqkf","tlqkf")

 #   def print_btn2(self):
        
#    def print_btn3(self):
        

if __name__ == '__main__':

#    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!
"""
"""
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 240, 731, 301))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_7 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_3.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_3.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_3.addWidget(self.pushButton_9)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(510, 180, 118, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menugd = QtWidgets.QMenu(self.menubar)
        self.menugd.setObjectName("menugd")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menugd.addSeparator()
        self.menugd.addSeparator()
        self.menubar.addAction(self.menugd.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_4.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_6.setText(_translate("MainWindow", "PushButton"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_7.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_8.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_9.setText(_translate("MainWindow", "PushButton"))
        self.menugd.setTitle(_translate("MainWindow", "코드 깔끔"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
"""