import numpy as np

test_board = [
    [0, 0, 0, 2, 6, 0, 7, 0, 1],
    [6, 8, 0, 0, 7, 0, 0, 9, 0],
    [1, 9, 0, 0, 0, 4, 5, 0, 0],
    [8, 2, 0, 1, 0, 0, 0, 4, 0],
    [0, 0, 4, 6, 0, 2, 9, 0, 0],
    [0, 5, 0, 0, 0, 3, 0, 2, 8],
    [0, 0, 9, 3, 0, 0, 0, 7, 4],
    [0, 4, 0, 0, 5, 0, 0, 3, 6],
    [7, 0, 3, 0, 1, 8, 0, 0, 0]
]

class SudokuBoard:
    def __init__(self, board):
        self.board = np.array(board)
        self.solved = False
        self.__empty_space = None

    def show_board(self):
        """Print the board"""
        for _row in range(len(self.board)):
            if _row % 3 == 0 and _row != 0:
                print('- - - - - - - - - - -')
            for _col in range(len(self.board[_row])):
                if _col % 3 == 0 and _col != 0 and _col != len(self.board[_row]):
                    print('|', end=' ')
                print(self.board[_row][_col], end=' ')
                if _col == len(self.board[_row])-1:
                    print('')

    def __get_empty_space(self):
        """Gets row and col location of first empty position"""
        _iter = np.nditer(self.board, flags=['multi_index'])
        for i in _iter:
            if i == 0:
                self.__empty_space = _iter.multi_index
                return self.__empty_space
        self.__empty_space = None
        return self.__empty_space

    def __update_solved(self):
        if self.__get_empty_space() is None:
            self.solved = True
            self.show_board()
            return self.solved

    def start(self):
        print('1')
        if self.__update_solved():  # updates solved status and empty space property
            print('2')
            return self.solved   # ends if there are no more empty spaces

        for i in range(1, 10):

            if self.is_valid(i):
                print('3')
                if self.start():
                    return self.solved
            else:
                print('4')
                self.board[self.__empty_space] = 0
        return self.solved

    def is_valid(self, num):
        self.board[self.__empty_space] = num    # inserts number to be tested into board
        validators = {'row': self.validate_row(num)}

        if not validators['row']:
            return False

        validators['col'] = self.validate_col(num)
        if not validators['col']:
            return False

        validators['square'] = self.validate_square(num)
        if not validators['square']:
            return False

        self.board[self.__empty_space] = num
        print('emptyspace', self.__empty_space, 'board', self.board)
        return True

    def validate_row(self, num):
        # Evaluates if the number which was added is valid for the row
        _iter_row = np.nditer(self.board[self.__empty_space[0]], flags=['f_index'])
        _row_is_valid = True
        for i in _iter_row:
            if i == num and _iter_row.index != self.__empty_space[1]:
                _row_is_valid = False
        return _row_is_valid

    def validate_col(self, num):
        _iter_col = np.nditer(self.board[:, self.__empty_space[1]], flags=['f_index'])
        _col_is_valid = True

        for i in _iter_col:
            if i == num and _iter_col.index != self.__empty_space[0]:
                _col_is_valid = False
        return _col_is_valid

    def validate_square(self, num):
        _square_is_valid = False
        _square = (self.__empty_space[0] // 3, self.__empty_space[1] // 3) # square as tuple (row(0, 1, 2), column)
        _iter_x = np.nditer(self.board[_square[0]*3: _square[0]*3 + 3, _square[1]*3: _square[1]*3 + 3], flags=['multi_index'])

        count = 0
        for i in _iter_x:
            if i == num:
                count += 1
        if count == 1:
            _square_is_valid = True
        return _square_is_valid

sud = SudokuBoard(test_board)
sud.show_board()
sud.start()
sud.show_board()