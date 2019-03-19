
# coding: utf-8

# In[ ]:


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QFont


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        QToolTip.setFont(QFont('SansSerif', 10))
#        self.setToolTip('This is a <b>QWidget</b> widget')

        self.statusBar().showMessage('연습 중..')

        btn = QPushButton('버튼1', self)
        btn2 = QPushButton('버튼2', self)
        btn3 = QPushButton('버튼3', self)
        btn.move(50, 100)
        btn2.move(150, 100)
        btn3.move(250, 100)
        
        btn.resize(btn.sizeHint())
        btn2.resize(btn.sizeHint())
        btn3.resize(btn.sizeHint())



        self.setWindowTitle('Ptolemy')
        self.setGeometry(500, 500, 500, 200)
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

