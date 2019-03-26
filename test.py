from PyQt5 import QtCore, QtGui, QtWidgets


class ui_mainwindow(object):

    def setup_ui(self, mainwindow):
        mainwindow.setObjectName("mainwindow")
        mainwindow.resize(500, 400)
        self.centralwidget = QtWidgets.QWidget(mainwindow)
        self.centralwidget.setObjectName("centralwidget")
        
        """
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 240, 731, 301))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(300, 200, 10, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.h_layout = QtWidgets.QHBoxLayout()
        self.h_layout.setObjectName("h_layout")        
        self.add_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.add_button.setObjectName("add_button")
        #self.verticalLayout.addWidget(self.add_button)
        self.h_layout.addWidget(self.add_button)
        self.select_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.select_button.setObjectName("select_button")
        self.h_layout.addWidget(self.select_button)
        self.delete_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.delete_button.setObjectName("delete_button")
        self.h_layout.addWidget(self.delete_button)
        self.verticalLayout.addLayout(self.h_layout)
        """
        
        ## layout
        self.h_layout_widget = QtWidgets.QWidget(self.centralwidget)
        self.h_layout_widget.setGeometry(QtCore.QRect(10, 10, 450, 350))
        self.h_layout_widget.setObjectName("h_layout_widget")
        self.h_layout = QtWidgets.QHBoxLayout(self.h_layout_widget)
        self.h_layout.setContentsMargins(0, 0, 0, 0)
        self.h_layout.setObjectName("h_layout")


        self.v_layout_1 = QtWidgets.QVBoxLayout()
        self.v_layout_2 = QtWidgets.QVBoxLayout()
        self.v_layout_1.setObjectName("v_layout_1")
        self.v_layout_2.setObjectName("v_layout_2")        

        #listview
        self.list = QtWidgets.QListView(self.v_layout_1)
        self.list.resize(400,300)
        #self.model = QtWidget.QstandardItem()
        
        #self.h_layout.addWidget(self.list)
        #self.list.setModel(self.model)


        ##button

        self.add_button = QtWidgets.QPushButton(self.h_layout_widget)
        self.add_button.setObjectName("add_button")
        self.add_button.move(200,10)
        self.add_button.resize(10,30)
        #self.v_layout.

        #self.verticalLayout.addWidget(self.add_button)
        self.v_layout.addWidget(self.add_button)
        self.select_button = QtWidgets.QPushButton(self.h_layout_widget)
        self.select_button.setObjectName("select_button")
        self.v_layout.addWidget(self.select_button)
        self.delete_button = QtWidgets.QPushButton(self.h_layout_widget)
        self.delete_button.setObjectName("delete_button")
        self.v_layout.addWidget(self.delete_button)
        self.h_layout.addLayout(self.v_layout)

        mainwindow.setCentralWidget(self.centralwidget)
        

        ## menubar
        self.menubar = QtWidgets.QMenuBar(mainwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        
        self.file_menu = QtWidgets.QMenu(self.menubar)
        self.file_menu.setObjectName("file_menu")
        
        mainwindow.setMenuBar(self.menubar)
        
        ## statusbar 

        self.statusbar = QtWidgets.QStatusBar(mainwindow)
        self.statusbar.setObjectName("statusbar")
        mainwindow.setStatusBar(self.statusbar)
        
        self.file_menu.addSeparator()
        self.file_menu.addSeparator()
        
        self.menubar.addAction(self.file_menu.menuAction())

        self.retranslateUi(mainwindow)
        
        QtCore.QMetaObject.connectSlotsByName(mainwindow)

    def retranslateUi(self, mainwindow):
        _translate = QtCore.QCoreApplication.translate
        mainwindow.setWindowTitle(_translate("mainwindow", "mainwindow"))
        
        self.add_button.setText(_translate("mainwindow", "add"))

        self.select_button.setText(_translate("mainwindow", "select"))
        self.select_button.resize(self.select_button.sizeHint())
        
        self.delete_button.setText(_translate("mainwindow", "delete"))
        self.delete_button.resize(self.delete_button.sizeHint())
        
        self.file_menu.setTitle(_translate("MainWindow", "File"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = QtWidgets.QMainWindow()
    ui = ui_mainwindow()
    ui.setup_ui(mainwindow)
    mainwindow.show()
    sys.exit(app.exec_())