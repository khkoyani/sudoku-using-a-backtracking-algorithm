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
np_board = np.array(test_board)

def show_board(b):
    """Print the board"""
    for _i in range(len(b)):
        if _i % 3 == 0 and _i != 0:
            print('- - - - - - - - - - -')
        for _cell in range(len(b[_i])):
            if _cell % 3 == 0 and _cell != 0 and _cell != len(b[_i]):
                print('|', end=' ')
            print(b[_i][_cell], end=' ')
            if _cell == len(b[_i])-1:
                print('')

def get_empty_space(b):
    """Gets row and col location of first empty position"""
    _iter = np.nditer(b, flags=['multi_index'])
    empty_spaces = []
    for i in _iter:
        if i == 0:
            return _iter.multi_index
    return None

def validate_row(b, num, loc):
    # Evaluates if the number which was added is valid for the row
    _iter_row = np.nditer(b[loc[0]], flags=['f_index'])
    _row_is_valid = True
    for i in _iter_row:
        if i == num and _iter_row.index != loc[1]:
            _row_is_valid = False
    return _row_is_valid

def validate_col(b, num, loc):
    _iter_col = np.nditer(b[:,loc[1]], flags=['f_index'])
    _col_is_valid = True

    for i in _iter_col:
        if i == num and _iter_col.index != loc[0]:
            _col_is_valid = False
    return _col_is_valid

def validate_square(b, num, loc):
    _square_is_valid = False
    _square = (loc[0] // 3, loc[1] // 3) # square as tuple (row(0, 1, 2), column)
    _iter_x = np.nditer(b[_square[0]*3: _square[0]*3 + 3, _square[1]*3: _square[1]*3 + 3], flags=['multi_index'])

    count = 0
    for i in _iter_x:
        if i == num:
            count += 1
    if count == 1:
        _square_is_valid = True
    return _square_is_valid

def is_valid(b, num, loc):
    b[loc] = num    # inserts number to be tested into board
    validators = {}

    validators['row'] = validate_row(b, num, loc)
    if not validators['row']:
        return False

    validators['col'] = validate_col(b, num, loc)
    if not validators['col']:
        return False

    validators['square'] = validate_square(b, num, loc)
    if not validators['square']:
        return False
    return True

def start(b):
    empty_space = get_empty_space(b)
    _finished = False
    if empty_space is None:
        _finished = True
        return _finished, b     # ends if there are no more empty spaces

    for i in range(1, 10):
        if is_valid(b, i, empty_space):
            b[empty_space] = i
            if start(b):
                _finished = True
                return _finished, b
        else:
            b[empty_space] = 0

    return _finished


finished, solved_board = start(np_board)
show_board(solved_board)

