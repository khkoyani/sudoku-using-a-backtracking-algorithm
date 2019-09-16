from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys



class Window(QMainWindow):
    """creates window to hold UI components"""
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(int(1920/3), 100, 800, 800)
        self.setWindowTitle('Sudoku and PyQt docs')
        self.populate_window()

    def populate_window(self):
        """Sets up the initial components"""
        self.label=QtWidgets.QLabel(self)
        self.label.setText('Is this working')
        self.label.move(100, 100)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText('Q Push Button')
        self.b1.move(100, 130)
        self.b1.clicked.connect(self.click_handler)

    def click_handler(self):
        self.label.setText('Button was clicked. Is it causing label resizing problems?')
        self.update()

    def update(self):
        self.label.adjustSize()
        self.label.move(70, 100)



def start():
    app = QApplication(sys.argv)     # passing empty list also works if not adding specific arguments
    win = Window()
    win.show()
    sys.exit(app.exec_())

start()