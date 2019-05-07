# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'keyboard.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets,Qt
import keyboard
import Macro

class EventHook:
    def __init__(self,ui):
        self.x_pos = None
        self.y_pos = None
        self.key = None
        self.ui = ui
    def KeyboardEvent(self, event):
        self.key = event.name
        print(str(self.key))
        self.ui.label_2.setText(str(event.name))
    
    def startKeyboardHook(self):
        keyboard.on_press(self.KeyboardEvent)
    
    def stopKeyboardHook(self):
        keyboard.unhook_all()

class keyboard_ui(object):
    def __init__(self):
        self.kh = EventHook(self)
        self.macro = Macro.Macro()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(195, 122)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 30, 60, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 30, 60, 20))
        self.label_2.setObjectName("label_2")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(20, 80, 156, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        self.kh.startKeyboardHook()
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "키 입력"))
        self.label_2.setText(_translate("Dialog", "키를 입력하세요"))




    def __del__(self):
        self.kh.stopKeyboardHook()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = keyboard_ui()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
