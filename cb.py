import numpy as np



class SudokuBoard:
    def __init__(self, board=None):
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

        if board:
            self.board = np.array(board).reshape((9,9))
        else:
            self.board = np.array(test_board).reshape((9,9))
        self.solved = False

    def get_board(self):
        return self.board

    def start(self):
        empty_space = self.get_empty_space()
        _finished = False
        if empty_space is None:
            _finished = True
            return _finished, self.board     # ends if there are no more empty spaces

        for i in range(1, 10):
            if self.is_valid(i, empty_space):
                self.board[empty_space] = i
                if self.start():
                    _finished = True
                    return _finished, self.board
            else:
                self.board[empty_space] = 0

        return _finished

    def validate_row(self, num, loc):
        # Evaluates if the number which was added is valid for the row
        _iter_row = np.nditer(self.board[loc[0]], flags=['f_index'])
        _row_is_valid = True
        for i in _iter_row:
            if i == num and _iter_row.index != loc[1]:
                _row_is_valid = False
        return _row_is_valid

    def validate_col(self, num, loc):
        _iter_col = np.nditer(self.board[:,loc[1]], flags=['f_index'])
        _col_is_valid = True

        for i in _iter_col:
            if i == num and _iter_col.index != loc[0]:
                _col_is_valid = False
        return _col_is_valid

    def validate_square(self, num, loc):
        _square_is_valid = False
        _square = (loc[0] // 3, loc[1] // 3) # square as tuple (row(0, 1, 2), column)
        _iter_x = np.nditer(self.board[_square[0]*3: _square[0]*3 + 3, _square[1]*3: _square[1]*3 + 3], flags=['multi_index'])

        count = 0
        for i in _iter_x:
            if i == num:
                count += 1
        if count == 1:
            _square_is_valid = True
        return _square_is_valid

    def is_valid(self, num, loc):
        self.board[loc] = num    # inserts number to be tested into board
        validators = {'row': self.validate_row(num, loc)}
        if not validators['row']:
            return False

        validators['col'] = self.validate_col(num, loc)
        if not validators['col']:
            return False

        validators['square'] = self.validate_square(num, loc)
        if not validators['square']:
            return False

        return True


    def get_empty_space(self):
        """Gets row and col location of first empty position"""
        _iter = np.nditer(self.board, flags=['multi_index'])
        for i in _iter:
            if i == 0:
                return _iter.multi_index
        return None

    def show_board(self):
        """Print the board"""
        for _i in range(len(self.board)):
            if _i % 3 == 0 and _i != 0:
                print('- - - - - - - - - - -')
            for _cell in range(len(self.board[_i])):
                if _cell % 3 == 0 and _cell != 0 and _cell != len(self.board[_i]):
                    print('|', end=' ')
                print(self.board[_i][_cell], end=' ')
                if _cell == len(self.board[_i])-1:
                    print('')

