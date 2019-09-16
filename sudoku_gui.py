from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGridLayout, QPushButton, QWidget, QLineEdit


def centered(self):
    self.setAlignment(QtCore.Qt.AlignCenter)

def get_font_with_size(size):
    default_size = 12
    font = QtGui.QFont()
    font.setFamily("Times New Roman")
    if type(size) is int:
        font.setPointSize(size)
    else:
        font.setPointSize(default_size)
    return font

class MyQLineEdit(QLineEdit):
    def __init__(self, name, *args, **kwargs):
        super(MyQLineEdit, self).__init__(*args, **kwargs)
        self.setObjectName(name)
        self.setFixedSize(QtCore.QSize(40, 40))
        # self.setMaximumSize(QtCore.QSize(40, 40))
        centered(self)
        self.setMaxLength(1)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.setup_main_window(MainWindow)
        self.setup_grid()
        self.setup_empty_board()
        self.setup_solve_btn()
        self.setup_title()



        self.gridLayoutWidget.adjustSize()


    def setup_solve_btn(self):
        self.solve_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.solve_btn.setMinimumSize(QtCore.QSize(100, 50))
        self.solve_btn.setFont(get_font_with_size(20))
        self.solve_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.solve_btn.setObjectName("solve_btn")
        self.solve_btn.setText('Solve Problem')
        self.grid.addWidget(self.solve_btn, 11, 3, 1, 5)
        self.solve_btn.adjustSize()

    def setup_empty_board(self):
        self.boxes = []
        for i in range(0, 9):
            self.boxes.append([])
            for y in range(0, 9):
                self.boxes[i].append(MyQLineEdit(parent=self.gridLayoutWidget, name='cell_'+str(i)+str(y)))
                self.grid.addWidget(self.boxes[i][y], i+1, y+1)

    def setup_grid(self):
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(150, 150, 600, 600))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.grid = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.grid.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.grid.setContentsMargins(10, 10, 10, 10)
        self.grid.setHorizontalSpacing(5)
        self.grid.setObjectName("grid")

    def setup_main_window(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

    def setup_title(self):
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(220, 80, 151, 21))
        self.Title.setMouseTracking(True)
        self.Title.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Title.setLineWidth(5)
        self.Title.setTextFormat(QtCore.Qt.RichText)
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        self.Title.setFont(get_font_with_size(30))
        self.Title.setText('Sudoku and PyQt')
        self.Title.adjustSize()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
