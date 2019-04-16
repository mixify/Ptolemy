import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class App(QWidget):
    def __init__(self, parent=None):
        super(App, self).__init__(parent=parent)  # these values change where the main window is placed
        self.title = 'This is my title'
        self.left = 400
        self.top = 400
        self.width = 300
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # call the gridlayout function
        self.createGridLayout()
        self.time_label.text = 'change the value'
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)
        self.show()  # this sets the main window to the screen size

    def createGridLayout(self):
        time = self.getTime()
        self.time_label = QLabel(time, self)
        self.horizontalGroupBox = QGroupBox()
        layout = QGridLayout()
        layout.addWidget(QPushButton('1'), 0, 0)
        layout.addWidget(QPushButton(time), 0, 1)
        layout.addWidget(self.time_label, 0, 2)
        self.horizontalGroupBox.setLayout(layout)

    def getTime(self):
        time = QTime.currentTime().toString()
        return time

    def updateTime(self):
        time = QTime.currentTime().toString()
        print("Time: " + time)
        self.time_label.setText(time)
        return time


def main():
    app = QApplication(sys.argv)
    ex = App()

    timer = QTimer()
  #  timer.timeout.connect(ex.updateTime)
    timer.start(1000)

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()