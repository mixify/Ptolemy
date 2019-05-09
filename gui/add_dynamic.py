from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtWidgets import QWidget
import mouse_ui,keyboard_ui,add_normal

class add_dynamic(object):
    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(340, 620)
       
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 321, 591))
        self.groupBox.setObjectName("groupBox")
        
        self.pushButton_1 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_1.setGeometry(QtCore.QRect(110, 30, 75, 30))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 30, 75, 30))
        self.pushButton_2.setObjectName("pushButton_2")

        self.label_1 = QtWidgets.QLabel(self.groupBox)
        self.label_1.setGeometry(QtCore.QRect(20, 30, 61, 30))
        self.label_1.setObjectName("label_1")

        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 540, 61, 30))
        self.label_2.setObjectName("label_2")
        
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(110, 540, 75, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(200, 540, 75, 30))
        self.pushButton_4.setObjectName("pushButton_4")

        self.groupBox_1 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_1.setGeometry(QtCore.QRect(10, 80, 291, 451))
        self.groupBox_1.setObjectName("groupBox_1")
        self.label_3 = QtWidgets.QLabel(self.groupBox_1)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 81, 30))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_1)
        self.label_4.setGeometry(QtCore.QRect(10, 250, 81, 30))
        self.label_4.setObjectName("label_4")

        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_1)
        self.pushButton_5.setGeometry(QtCore.QRect(110, 40, 75, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_1)
        self.pushButton_6.setGeometry(QtCore.QRect(110, 250, 75, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        
        self.graphicsView = QtWidgets.QGraphicsView(self.groupBox_1)
        self.graphicsView.setGeometry(QtCore.QRect(10, 70, 271, 161))
        self.graphicsView.setObjectName("graphicsView")
        
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.groupBox_1)
        self.graphicsView_2.setGeometry(QtCore.QRect(10, 280, 271, 161))
        self.graphicsView_2.setObjectName("graphicsView_2")
        
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_7.setGeometry(QtCore.QRect(250, 570, 75, 20))
        self.pushButton_7.setObjectName("pushButton_7")
#        self.pushButton_10 = QtWidgets.QPushButton(Dialog)
#        self.pushButton_10.setGeometry(QtCore.QRect(520, 610, 75, 23))
#        self.pushButton_10.setObjectName("pushButton_10")


        self.pushButton_1.clicked.connect(self.normal_setting)
        self.pushButton_3.clicked.connect(self.normal_setting)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "매크로 만들기"))
        
        self.groupBox.setTitle(_translate("Dialog", "다이나믹 매크로"))
        self.label_1.setText(_translate("Dialog", "시작매크로"))
        self.pushButton_1.setText(_translate("Dialog", "만들기"))
        self.pushButton_2.setText(_translate("Dialog", "불러오기"))


        self.label_2.setText(_translate("Dialog", "종료매크로"))
        self.pushButton_3.setText(_translate("Dialog", "만들기"))
        self.pushButton_4.setText(_translate("Dialog", "불러오기"))
        
        self.groupBox_1.setTitle(_translate("Dialog", "학습요인 설정"))
        self.label_3.setText(_translate("Dialog", "화면 설정"))
        self.pushButton_5.setText(_translate("Dialog", "설정하기"))
      
        self.label_4.setText(_translate("Dialog", "키 설정"))
        self.pushButton_6.setText(_translate("Dialog", "설정하기"))


        self.pushButton_7.setText(_translate("Dialog", "저장하기"))


    def normal_setting(self):
        Dialog = QtWidgets.QDialog()
        ui = add_normal.add_normal()
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
    ui = add_dynamic()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())