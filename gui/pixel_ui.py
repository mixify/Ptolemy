
from PyQt5 import QtCore, QtGui, QtWidgets


class delay_ui(object):
    delay = None
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(250, 200)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(80, 170,75 , 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 170, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 40, 80, 20))
        self.label.setObjectName("label")

        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(100,40,60,20))
        self.pushButton_3.setObjectName("pushButton_3")
        
        
        
        
        
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 90, 20))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(105, 80, 40, 20))
        self.lineEdit_2.setObjectName("lineEdit")
        
      #  self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
      #  self.lineEdit_2.setGeometry(QtCore.QRect(50, 60, 113, 20))
      #  self.lineEdit_2.setObjectName("lineEdit")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.reject)
        self.pushButton_2.clicked.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "픽셀 검출 보상 설정"))
        self.pushButton.setText(_translate("Dialog","확인"))
        self.pushButton_2.setText(_translate("Dialog","취소"))
        
        self.label.setText(_translate("Dialog", "픽셀 위치 지정 :"))
        self.pushButton_3.setText(_translate("Dialog","설정하기"))
        self.label_3.setText(_translate("Dialog", "픽셀 보상 설정"))
            





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = delay_ui()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
