# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mouse.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets 

import mouse
import keyboard
import Macro

class mouseHook:
   # def __init__(self):
   #     self.x_pos = None
   #     self.y_pos = None

    def __init__(self,ui):
        self.ui = ui
        self.x_pos = None
        self.y_pos = None

    def MouseEvent(self, event):
        if isinstance(event, mouse.MoveEvent):
            self.x_pos = event.x
            self.y_pos = event.y
            self.ui.label_4.setText(str(self.x_pos))
            self.ui.label_5.setText(str(self.y_pos))
           # print(self.x_pos)
    
    def startHook(self):
        mouse.hook(self.MouseEvent)

    def stopHook(self):
       # keyboard.wait('esc')
        mouse.unhook(self.MouseEvent)
   
#    def update_mouse(self,Dialog):
#        self.x_pos = event.x
#        Dialog.setText(mh.x_pos)


class mouse_ui(object):
    def __init__(self):
        self.mh = mouseHook(self)
  #      self.macro = Macro.Macro(self)
     #     self.setupUi(self)
        self.macro = Macro.Macro()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(180, 220)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 101, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 16, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(80, 40, 16, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 40, 31, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(100, 40, 31, 16))
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(10, 70, 161, 16))
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(10, 100, 16, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(80, 100, 16, 16))
        self.label_10.setObjectName("label_10")
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(30, 100, 42, 22))
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setMaximum(1920)
        self.spinBox_2 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_2.setGeometry(QtCore.QRect(100, 100, 42, 22))
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_2.setMaximum(1080)
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(90, 140, 76, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(10, 140, 81, 16))
        self.label_8.setObjectName("label_8")


        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 180, 156, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        
        self.buttonBox.accepted.connect(self.return_spinboxvalue)
        self.buttonBox.rejected.connect(Dialog.reject)
        
        self.retranslateUi(Dialog)

  #      self.label_4.mouseMoveEvent(self.label_4,mh.startHook)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.mh.startHook()
        self.label.setText(_translate("Dialog", "현재 마우스 좌표"))
        self.label_2.setText(_translate("Dialog", "x :"))
        self.label_3.setText(_translate("Dialog", "y :"))
        #self.label_4.setText(_translate("Dialog", str(self.mh.x_pos)))
        #self.label_5.setText(_translate("Dialog", str(self.mh.y_pos)))
        self.label_7.setText(_translate("Dialog", "매크로 마우스 좌표 설정하기"))
        self.label_9.setText(_translate("Dialog", "x :"))
        self.label_10.setText(_translate("Dialog", "y :"))
        self.comboBox.setItemText(0, _translate("Dialog", "이동"))
        self.comboBox.setItemText(1, _translate("Dialog", "좌클릭"))
        self.comboBox.setItemText(2, _translate("Dialog", "우클릭"))
        self.comboBox.setItemText(3, _translate("Dialog", "드레그 시작"))
        self.comboBox.setItemText(4, _translate("Dialog", "드레그 끝"))
        self.label_8.setText(_translate("Dialog", "마우스 동작"))

    def return_spinboxvalue(self):
        a=[]
        a.append(self.spinBox.value())
        a.append(self.spinBox_2.value())
        b = str(self.comboBox.currentText())
        if b=="이동":
            self.macro.setMouseMove(a[0],a[1])
        if b=="좌클릭":
            self.macro.setMouseMove(a[0],a[1])
            self.macro.setMouseClick("left")
        if b=="우클릭":
            self.macro.setMouseMove(a[0],a[1])
            self.macro.setMouseClick("right")

        self.macro.runMacro()
    def __del__(self):
        self.mh.stopHook()
if __name__ == "__main__":
#    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
 #  mh = mouseHook()
  #  mh.startHook()  
    ui = mouse_ui()
    ui.setupUi(Dialog)
    Dialog.show()  
    sys.exit(app.exec_())
   # mh.stopHook()
    
