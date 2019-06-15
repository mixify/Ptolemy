
from PyQt5 import QtCore, QtGui, QtWidgets


class delay_ui(object):
    delay = None
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(203, 147)
  #      self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
  #      self.buttonBox.setGeometry(QtCore.QRect(20, 100, 161, 32))
  #      self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
  #      self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
  #      self.buttonBox.setObjectName("buttonBox")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(40, 120, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 120, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 60, 41, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(170, 60, 21, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(50, 60, 113, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(self.clicked_button)
        self.pushButton.clicked.connect(Dialog.reject)
        self.pushButton_2.clicked.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog","확인"))
        self.pushButton_2.setText(_translate("Dialog","취소"))
        
        self.label.setText(_translate("Dialog", "딜레이"))
        self.label_2.setText(_translate("Dialog", "초"))

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
