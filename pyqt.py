from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app = QApplication(sys.argv)     # passing empty list also works if not adding specific arguments
    win = QMainWindow() #wraps QToolbars,QdockWidget,Qmenu, QstatusBar, QCENTRALwIDGET
    win.setGeometry(1920/3, 100, 800, 800)
    win.setWindowTitle('Sudoku and PyQt docs')

    label=QtWidgets.QLabel(win)
    label.setText('Is this working')
    label.move(100, 100)

    win.show()
    sys.exit(app.exec_())

window()