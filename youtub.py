import sys
#from PyQt5.QtWidgets import QApplication, QMainWindow,QAction,QMenu ,QWidget, QPushButton, QMessageBox
#from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtCore, QtGui, QtWidgets


#일반적인 창.
class test_main(QtWidgets.QMainWindow):
    def __init__(self) :
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.statusBar()
        self.statusBar().showMessage("대기")
        
        menu = self.menuBar()
        menu_file = menu.addMenu("File")
        
        file_exit = QtWidgets.QAction("Exit",self)
        file_exit.setShortcut("Ctrl+Q")
        file_exit.setStatusTip("누르면 꺼진다.")

        file_exit.triggered.connect(QtCore.QCoreApplication.instance().quit)

        new_learning_macro = QtWidgets.QAction("러닝 매크로 만들기",self)
        new_macro = QtWidgets.QAction("매크로 만들기",self)
        
        file_new = QtWidgets.QMenu("New",self)
        file_new.addAction(new_learning_macro)
        file_new.addAction(new_macro)

        menu_file.addMenu(file_new)
        menu_file.addAction(file_exit)

        btn = QPushButton("rlqkf")
        """self.home_ui()
    def home_ui(self):
        btn = QtWidgets.QPushButton("quit",self)
        btn.resize(btn.sizeHint())#글씨로 크기조절
        btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        #btn.setToolTip("연습하고있따.")
        btn.move(20,50)
        
    def closeEvent(self,QCloseEvent):
        ans = QtWidgets.QMessageBox.question(self,"종료 확인","종료하시겠습니까?",
        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.Yes)

        if ans == QtWidgets.QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()
        """

        self.resize(700,500)
        self.setWindowTitle("REAL")
        self.show()



app = QtWidgets.QApplication(sys.argv) #만드시 어플리케이션 객체 생성
w = test_main()
sys.exit(app.exec_())