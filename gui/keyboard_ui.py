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
        self.return_val = None
    def KeyboardEvent(self, event):
        self.key = event.name
        print(str(self.key))
        self.ui.input_key.setText(str(event.name))
    
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
        self.input_key = QtWidgets.QLineEdit(Dialog)
        self.input_key.setGeometry(QtCore.QRect(70, 30, 90, 20))
        self.input_key.setObjectName("input_key")
        self.input_key.setReadOnly(True)
        
    #   self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
    #    
        self.pushButton_1 = QtWidgets.QPushButton(Dialog)
        self.pushButton_1.setAutoDefault(False)
        self.pushButton_1.setGeometry(QtCore.QRect(20, 80, 80, 23))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 80, 80, 23))
        self.pushButton_2.setObjectName("pushButton_2")
   #     self.buttonBox.setStandardButtons(self.pushButton_1|self.pushButton_2)
      
     #   self.buttonBox.setObjectName("buttonBox")
        
        self.pushButton_1.clicked.connect(self.clicked_ok)
        self.pushButton_2.clicked.connect(Dialog.reject)
    
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        self.kh.startKeyboardHook()
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "키 입력"))
        self.input_key.setText(_translate("Dialog", "키를 입력하세요"))
        self.pushButton_1.setText(_translate("Dialog","확인"))
        self.pushButton_2.setText(_translate("Dialog","취소"))
    def clicked_ok(self):
        self.return_val = self.input_key.text()
        Dialog.reject()


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
