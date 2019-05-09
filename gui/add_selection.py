from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtWidgets import QWidget
import mouse_ui,keyboard_ui

class add_selection(object):
    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(250, 150)
       
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 230, 90))
        self.groupBox.setObjectName("groupBox")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(30, 30, 90, 15))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(30, 60, 110, 15))
        self.radioButton_2.setObjectName("radioButton_2")
    

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "매크로 만들기"))
        
        
        self.groupBox.setTitle(_translate("Dialog", "매크로 종류"))
        self.radioButton.setText(_translate("Dialog", "일반 매크로"))
        self.radioButton_2.setText(_translate("Dialog", "다이나믹 매크로"))
        
        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = add_selection()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())