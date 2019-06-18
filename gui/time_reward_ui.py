
from PyQt5 import QtCore, QtGui, QtWidgets


class delay_ui(object):
    delay = None
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(220, 150)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(40, 120, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 120, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 40, 60, 20))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(80, 40, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 65, 60, 20))
        self.label_3.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 65, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 90, 100, 20))
        self.label_4.setObjectName("label_2")
        self.cb = QtWidgets.QCheckBox(Dialog)
        self.cb.setGeometry(95,90,20,20)
    
      #  self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
      #  self.lineEdit_2.setGeometry(QtCore.QRect(50, 60, 113, 20))
      #  self.lineEdit_2.setObjectName("lineEdit")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(self.clicked_button)
        self.pushButton.clicked.connect(Dialog.reject)
        self.pushButton_2.clicked.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "시간 보상 설정"))
        self.pushButton.setText(_translate("Dialog","확인"))
        self.pushButton_2.setText(_translate("Dialog","취소"))
        
        self.label.setText(_translate("Dialog", "시작 시간 :"))
        self.label_3.setText(_translate("Dialog", "시간 간격 :"))
        self.label_4.setText(_translate("Dialog", "최대 시간 갱신"))

    def clicked_button(self,Dialog):
        if self.lineEdit.text():
            self.delay = self.lineEdit.text()
        

            





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = delay_ui()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
