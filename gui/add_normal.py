from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtWidgets import QWidget
import mouse_ui,keyboard_ui

class add_normal(object):
    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(611, 645)
       
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 120, 241, 381))
        self.groupBox_2.setObjectName("groupBox_2")
        
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 75, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 45, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_4.setGeometry(QtCore.QRect(120, 105, 75, 23))
        self.pushButton_4.setObjectName("pushButton_5")

        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_5.setGeometry(QtCore.QRect(120, 135, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")

        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(20, 45, 71, 20))
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(20, 75, 71, 20))
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(20, 105, 71, 20))
        self.label_3.setScaledContents(False)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(20, 135, 71, 20))
        self.label_4.setScaledContents(False)
        self.label_4.setObjectName("label_4")
        self.listView = QtWidgets.QListView(self.groupBox_2)
        self.listView.setGeometry(QtCore.QRect(10, 160, 221, 191))
        self.listView.setObjectName("listView")

        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(160, 335, 75, 23))
        self.pushButton.setObjectName("pushButton")
        
#        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
#        self.pushButton_4.setGeometry(QtCore.QRect(520, 610, 75, 23))
#        self.pushButton_4.setObjectName("pushButton_4")


        self.pushButton_2.clicked.connect(self.keyboard_setting)
        self.pushButton_3.clicked.connect(self.mouse_setting)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "매크로 만들기"))
        
        self.groupBox_2.setTitle(_translate("Dialog", "일반 매크로"))
        self.pushButton_2.setText(_translate("Dialog", "추가하기"))
        self.pushButton_3.setText(_translate("Dialog", "추가하기"))
        self.pushButton_4.setText(_translate("Dialog", "추가하기"))
        self.pushButton_5.setText(_translate("Dialog", "추가하기"))

        self.label.setText(_translate("Dialog", "마우스 설정"))
        self.label_2.setText(_translate("Dialog", "키보드 설정"))
        self.label_3.setText(_translate("Dialog","딜레이 설정"))
        self.label_4.setText(_translate("Dialog", "녹화 설정"))

        self.pushButton.setText(_translate("Dialog", "저장하기"))


    def keyboard_setting(self):
        Dialog = QtWidgets.QDialog(self.pushButton_4)
        ui = keyboard_ui.keyboard_ui()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()

    def mouse_setting(self):
        Dialog = QtWidgets.QDialog()
        ui = mouse_ui.mouse_ui()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()
        
        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = add_normal()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())