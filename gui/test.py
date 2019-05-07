import sys
from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtWidgets import QMessageBox
import keyboard
import mouse
import Macro

class Ui_MainWindow(object):


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(740, 640)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 721, 541))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")


        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)


        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)

        self.listView = QtWidgets.QListView(self.gridLayoutWidget)
        self.listView.setObjectName("listView")
        self.gridLayout.addWidget(self.listView, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)


        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 725, 21))
        self.menubar.setObjectName("menubar")


        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")


        self.menu = QtWidgets.QMenu(self.menuFile)
        self.menu.setObjectName("menu")


        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.action_6 = QtWidgets.QAction(MainWindow)
        self.action_6.setObjectName("action_6")
        self.action_7 = QtWidgets.QAction(MainWindow)
        self.action_7.setObjectName("action_7")
        self.action_8 = QtWidgets.QAction(MainWindow)
        self.action_8.setObjectName("action_8")
        
        
        self.menu.addAction(self.action_7)
        self.menu.addAction(self.action_8)
        
        
        self.menuFile.addAction(self.menu.menuAction())
        self.menuFile.addAction(self.action_2)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_4)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_6)
        
        
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)

        self.pushButton_2.clicked.connect(self.add_button_clicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.pushButton_2.setText(_translate("MainWindow", "추가"))
        self.pushButton.setText(_translate("MainWindow", "실행"))
        self.pushButton_3.setText(_translate("MainWindow", "수정"))
        self.pushButton_4.setText(_translate("MainWindow", "삭제"))
        
        
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menu.setTitle(_translate("MainWindow", "새 매크로 만들기"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))


        self.action_2.setText(_translate("MainWindow", "매크로 불러오기"))
        self.action_4.setText(_translate("MainWindow", "단축키 설정"))
        self.action_6.setText(_translate("MainWindow", "종료"))
        self.action_7.setText(_translate("MainWindow", "일반 매크로 생성"))
        self.action_8.setText(_translate("MainWindow", "딥러닝 매크로 생성"))
    
    def add_button_clicked(self):
        Dialog = QtWidgets.QDialog(self.pushButton_2)
        ui = add_ui()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()


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
        self.groupBox_2.setGeometry(QtCore.QRect(10, 120, 241, 381))
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 75, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 45, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_10.setGeometry(QtCore.QRect(120, 105, 75, 23))
        self.pushButton_10.setObjectName("pushButton_12")
        self.pushButton_12 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_12.setGeometry(QtCore.QRect(120, 135, 75, 23))
        self.pushButton_12.setObjectName("pushButton_12")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(20, 45, 71, 20))
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(20, 75, 71, 20))
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(20, 105, 71, 20))
        self.label_11.setScaledContents(False)
        self.label_11.setObjectName("label_11")
        self.listView = QtWidgets.QListView(self.groupBox_2)
        self.listView.setGeometry(QtCore.QRect(10, 160, 221, 191))
        self.listView.setObjectName("listView")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(160, 335, 75, 23))
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


        self.pushButton_2.clicked.connect(self.keyboard_setting)
        self.pushButton_3.clicked.connect(self.mouse_setting)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "매크로 만들기"))
        self.groupBox.setTitle(_translate("Dialog", "매크로 종류"))
        self.radioButton.setText(_translate("Dialog", "일반 매크로"))
        self.radioButton_2.setText(_translate("Dialog", "다이나믹 매크로"))
        self.groupBox_2.setTitle(_translate("Dialog", "일반 매크로"))

        self.pushButton_2.setText(_translate("Dialog", "추가하기"))
        
        self.pushButton_3.setText(_translate("Dialog", "추가하기"))
        self.pushButton_10.setText(_translate("Dialog", "녹화하기"))
        self.pushButton_12.setText(_translate("Dialog", "설정하기"))

        self.label.setText(_translate("Dialog", "마우스 설정"))
        self.label_2.setText(_translate("Dialog", "키보드 설정"))
        
        self.label_11.setText(_translate("Dialog", "녹화 설정"))

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


    def keyboard_setting(self):
        Dialog = QtWidgets.QDialog(self.pushButton_10)
        ui = keyboard_ui()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()

    def mouse_setting(self):
        Dialog = QtWidgets.QDialog()
        ui = mouse_ui()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()
        
        
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

class EventHook:
    def __init__(self,ui):
        self.x_pos = None
        self.y_pos = None
        self.key = None
        self.ui = ui
    def KeyboardEvent(self, event):
        self.key = event.name
        print(str(self.key))
        self.ui.label_2.setText(str(event.name))
    
    def startKeyboardHook(self):
        keyboard.on_press(self.KeyboardEvent)
    
    def stopKeyboardHook(self):
        keyboard.unhook_all()

class keyboard_ui(object):
    def __init__(self):
        self.kh = EventHook(self)
        self.macro = Macro.Macro()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(195, 122)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 30, 60, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 30, 60, 20))
        self.label_2.setObjectName("label_2")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(20, 80, 156, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        self.kh.startKeyboardHook()
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "키 입력"))
        self.label_2.setText(_translate("Dialog", "키를 입력하세요"))




    def __del__(self):
        self.kh.stopKeyboardHook()




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
