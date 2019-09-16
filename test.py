# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(952, 889)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 160, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.group_box_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.group_box_2.setGeometry(QtCore.QRect(280, 360, 181, 71))
        self.group_box_2.setCheckable(False)
        self.group_box_2.setObjectName("group_box_2")
        self.box_3 = QtWidgets.QLineEdit(self.group_box_2)
        self.box_3.setGeometry(QtCore.QRect(110, 10, 40, 40))
        self.box_3.setMaximumSize(QtCore.QSize(40, 40))
        self.box_3.setAlignment(QtCore.Qt.AlignCenter)
        self.box_3.setObjectName("box_3")
        self.box_2 = QtWidgets.QLineEdit(self.group_box_2)
        self.box_2.setGeometry(QtCore.QRect(60, 10, 40, 40))
        self.box_2.setMaximumSize(QtCore.QSize(40, 40))
        self.box_2.setAlignment(QtCore.Qt.AlignCenter)
        self.box_2.setObjectName("box_2")
        self.box_1 = QtWidgets.QLineEdit(self.group_box_2)
        self.box_1.setGeometry(QtCore.QRect(10, 10, 40, 40))
        self.box_1.setMaximumSize(QtCore.QSize(40, 40))
        self.box_1.setMaxLength(1)
        self.box_1.setCursorPosition(1)
        self.box_1.setAlignment(QtCore.Qt.AlignCenter)
        self.box_1.setObjectName("box_1")
        self.widget_container = QtWidgets.QWidget(self.centralwidget)
        self.widget_container.setGeometry(QtCore.QRect(270, 500, 241, 111))
        self.widget_container.setObjectName("widget_container")
        self.box_4 = QtWidgets.QLineEdit(self.widget_container)
        self.box_4.setGeometry(QtCore.QRect(120, 20, 40, 40))
        self.box_4.setMaximumSize(QtCore.QSize(40, 40))
        self.box_4.setAlignment(QtCore.Qt.AlignCenter)
        self.box_4.setObjectName("box_4")
        self.box_5 = QtWidgets.QLineEdit(self.widget_container)
        self.box_5.setGeometry(QtCore.QRect(70, 20, 40, 40))
        self.box_5.setMaximumSize(QtCore.QSize(40, 40))
        self.box_5.setAlignment(QtCore.Qt.AlignCenter)
        self.box_5.setObjectName("box_5")
        self.box_6 = QtWidgets.QLineEdit(self.widget_container)
        self.box_6.setGeometry(QtCore.QRect(20, 20, 40, 40))
        self.box_6.setMaximumSize(QtCore.QSize(40, 40))
        self.box_6.setMaxLength(1)
        self.box_6.setCursorPosition(1)
        self.box_6.setAlignment(QtCore.Qt.AlignCenter)
        self.box_6.setObjectName("box_6")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(360, 120, 151, 21))
        self.Title.setMouseTracking(True)
        self.Title.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Title.setLineWidth(5)
        self.Title.setTextFormat(QtCore.Qt.RichText)
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 952, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.pressed)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Solve"))
        self.group_box_2.setTitle(_translate("MainWindow", "GroupBox"))
        self.box_3.setText(_translate("MainWindow", "2"))
        self.box_2.setText(_translate("MainWindow", "1"))
        self.box_1.setText(_translate("MainWindow", "a"))
        self.box_6.setText(_translate("MainWindow", "a"))
        self.box_4.setText(_translate("MainWindow", "5"))
        self.box_5.setText(_translate("MainWindow", "4"))
        self.Title.setText(_translate("MainWindow", "Sudoku Board"))

    def pressed(self):
        for i in self.widget_container.children():
            print(i.objectName())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
