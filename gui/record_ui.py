# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'record.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import Macro
import keyboard,mouse

class record_ui(object):
    tmp = None
    Macro = Macro.Macro()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(250, 150)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 120, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(120, 120, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 56, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 56, 12))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(80, 20, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 60, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(self.startrecording)
        self.pushButton_3.clicked.connect(Dialog.accept)
        self.pushButton_2.clicked.connect(self.stoprecording)
        self.pushButton_4.clicked.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "녹화시작"))
        self.label_2.setText(_translate("Dialog", "녹화종료"))
        self.pushButton.setText(_translate("Dialog", "f1도 됩니다"))
        self.pushButton_2.setText(_translate("Dialog", "f2도 됩니다"))
 
    def startrecording(self,Dialog):
        self.Macro.startRecord()
    def stoprecording(self,Dialog):
        self.Macro.stopRecord()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = record_ui()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
