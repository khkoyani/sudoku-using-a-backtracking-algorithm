from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGridLayout, QPushButton, QWidget, QLineEdit
from cb import SudokuBoard


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
        centered(self)
        self.setFont(get_font_with_size(12))
        self.setMaxLength(1)

class MyButtons(QPushButton):
    def __init__(self, name, *args, **kwargs):
        super(MyButtons, self).__init__(*args, **kwargs)
        self.setMinimumSize(QtCore.QSize(100, 50))
        self.setFont(get_font_with_size(18))
        self.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.adjustSize()
        # self.solve_btn.setObjectName("solve_btn")
        # self.solve_btn.setText('Solve Problem')

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.setup_main_window(MainWindow)
        self.setup_grid()
        self.setup_empty_board()
        self.setup_solve_btn()
        self.set_test_board_btn()
        self.setup_title()

        self.gridLayoutWidget.adjustSize()

    def set_test_board(self, _type, _values=None):
        board = None
        if _type == 'test':
            game = SudokuBoard()
            board = game.get_board()
        if _type == 'solve':
            board = _values
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i, j] != 0:
                    self.boxes[i][j].setText(str(board[i, j]))
                else:
                    self.boxes[i][j].setText(None)

    def setup_solve_btn(self):
        self.solve_btn = MyButtons(parent=self.gridLayoutWidget, name="solve_btn", text='Solve Problem')
        self.grid.addWidget(self.solve_btn, 11, 6, 1, 4)
        self.solve_btn.clicked.connect(self.clicked_solve)

    def set_test_board_btn(self):
        self.test_board_btn = MyButtons(parent=self.gridLayoutWidget, name="test_board_btn", text='Create Test Board')
        self.grid.addWidget(self.test_board_btn, 11, 1, 1, 5)
        self.test_board_btn.clicked.connect(lambda: self.set_test_board('test'))

    def setup_empty_board(self):
        self.boxes = []
        for i in range(0, 9):
            self.boxes.append([])
            for y in range(0, 9):
                self.boxes[i].append(MyQLineEdit(parent=self.gridLayoutWidget, name='cell_'+str(i)+'_'+str(y)))
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

    def get_values_on_board(self):
        values = []
        for i in range(len(self.boxes)):
            for j in range(len(self.boxes[i])):
                _v = self.boxes[i][j].text()
                if _v:
                    values.append(int(_v))
                else:
                    values.append(0)
        return values

    def clicked_solve(self):
        board = SudokuBoard(self.get_values_on_board())
        ans = board.start()[1]
        self.set_test_board(_type='solve', _values=ans)
        # print(board.show_board())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
