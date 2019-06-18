from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtWidgets import QWidget
import add_normal,add_dynamic

class add_selection(object):
    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(250, 150)
       
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 230, 90))
        self.groupBox.setObjectName("groupBox")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(30, 30, 110, 15))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(30, 60, 110, 15))
        self.radioButton_2.setObjectName("radioButton_2")
    
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(40, 120, 75, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.next_dialog)


        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 120, 75, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "보상 선택"))
        
        
        self.groupBox.setTitle(_translate("Dialog", "보상 종류"))
        self.radioButton.setText(_translate("Dialog", "시간 지연 보상"))
        self.radioButton_2.setText(_translate("Dialog", "픽셀 검출 보상"))
        self.pushButton.setText(_translate("Dialog","확인"))
        self.pushButton_2.setText(_translate("Dialog","취소"))

    def next_dialog(self):
        Dialog = QtWidgets.QDialog()
        if self.radioButton.isChecked():
            ui = add_normal.add_normal()
        elif self.radioButton_2.isChecked():
            ui = add_dynamic.add_dynamic()

        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()            



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = add_selection()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())