from PyQt5 import QtCore, QtGui, QtWidgets
import mouse_ui,keyboard_ui


class add_ui(object):
    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(611, 645)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 241, 91))
        self.groupBox.setObjectName("groupBox")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(30, 30, 90, 16))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(30, 60, 111, 16))
        self.radioButton_2.setObjectName("radioButton_2")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 120, 241, 351))
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 80, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 50, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(20, 50, 71, 20))
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 71, 20))
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.listView = QtWidgets.QListView(self.groupBox_2)
        self.listView.setGeometry(QtCore.QRect(10, 130, 221, 181))
        self.listView.setObjectName("listView")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(160, 320, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(280, 10, 321, 591))
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_4.setGeometry(QtCore.QRect(110, 30, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(20, 30, 61, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(20, 540, 61, 21))
        self.label_5.setObjectName("label_5")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_5.setGeometry(QtCore.QRect(110, 540, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 80, 291, 451))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label_6.setGeometry(QtCore.QRect(10, 40, 81, 16))
        self.label_6.setObjectName("label_6")
        self.label_10 = QtWidgets.QLabel(self.groupBox_4)
        self.label_10.setGeometry(QtCore.QRect(10, 250, 81, 16))
        self.label_10.setObjectName("label_10")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_8.setGeometry(QtCore.QRect(110, 40, 75, 23))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_9.setGeometry(QtCore.QRect(110, 250, 75, 23))
        self.pushButton_9.setObjectName("pushButton_9")
        self.graphicsView = QtWidgets.QGraphicsView(self.groupBox_4)
        self.graphicsView.setGeometry(QtCore.QRect(10, 70, 271, 161))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.groupBox_4)
        self.graphicsView_2.setGeometry(QtCore.QRect(10, 280, 271, 161))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_11.setGeometry(QtCore.QRect(240, 560, 75, 23))
        self.pushButton_11.setObjectName("pushButton_11")
#        self.pushButton_10 = QtWidgets.QPushButton(Dialog)
#        self.pushButton_10.setGeometry(QtCore.QRect(520, 610, 75, 23))
#        self.pushButton_10.setObjectName("pushButton_10")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "매크로 종류"))
        self.radioButton.setText(_translate("Dialog", "일반 매크로"))
        self.radioButton_2.setText(_translate("Dialog", "다이나믹 매크로"))
        self.groupBox_2.setTitle(_translate("Dialog", "일반 매크로"))

        self.pushButton_2.setText(_translate("Dialog", "추가하기"))
        self.pushButton_2.clicked.connect(self.keyboard_setting)
        
        self.pushButton_3.setText(_translate("Dialog", "추가하기"))
        self.pushButton_3.clicked.connect(self.mouse_setting)

        self.label.setText(_translate("Dialog", "마우스 설정"))
        self.label_2.setText(_translate("Dialog", "키보드 설정"))
        self.pushButton.setText(_translate("Dialog", "저장하기"))
        self.groupBox_3.setTitle(_translate("Dialog", "다이나믹 매크로"))
        self.pushButton_4.setText(_translate("Dialog", "불러오기"))
        self.label_4.setText(_translate("Dialog", "시작매크로"))
        self.label_5.setText(_translate("Dialog", "종료매크로"))
        self.pushButton_5.setText(_translate("Dialog", "불러오기"))
        self.groupBox_4.setTitle(_translate("Dialog", "학습요인 설정"))
        self.label_6.setText(_translate("Dialog", "긍정요소 설정"))
        self.label_10.setText(_translate("Dialog", "부정요소 설정"))

        self.pushButton_8.setText(_translate("Dialog", "설정하기"))
        self.pushButton_9.setText(_translate("Dialog", "설정하기"))

        self.pushButton_11.setText(_translate("Dialog", "저장하기"))
    #    self.pushButton_10.setText(_translate("Dialog", "닫기"))

    def mouse_setting(self):
        Dialog = QtWidgets.QDialog(self.pushButton_3)
        ui = mouse_ui.mouse_ui()
        ui.setupUi(Dialog)
        print('tlqkf')
        Dialog.show()

    def keyboard_setting(self):
        Dialog = QtWidgets.QDialog(self.pushButton_2)
        ui = keyboard_ui.keyboard_ui()
        ui.setupUi(Dialog)
        Dialog.show()
        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = add_ui()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
