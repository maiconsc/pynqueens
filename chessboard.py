def create_board(n):
    """
    Draw a nxn empty chess board.
    :param n: size of the chess board (n columns x n rows)
    :return: string containing the empty chess board (unicode)
    """

    # internal methods
    def draw_top_border(columns):
        drawn_cols = 0
        str_top = '┌'
        while drawn_cols != columns:
            for j in range(0, 3):
                str_top += '─'
            drawn_cols += 1
            if columns == drawn_cols:
                str_top += '┐'
            else:
                str_top += '┬'
        return str_top

    def draw_bottom_border(columns):
        drawn_cols = 0
        str_bot = '└'
        while drawn_cols != columns:
            for j in range(0, 3):
                str_bot += '─'
            drawn_cols += 1
            if columns == drawn_cols:
                str_bot += '┘'
            else:
                str_bot += '┴'
        return str_bot

    def draw_middle_border(columns):
        drawn_cols = 0
        str_mid = '│'
        while drawn_cols != columns:
            for j in range(0, 3):
                str_mid += ' '
            str_mid += '│'
            drawn_cols += 1
        return str_mid

    def draw_cells_border(columns):
        drawn_cols = 0
        str_cells_b = '├'
        while drawn_cols != columns:
            for j in range(0, 3):
                str_cells_b += '─'
            drawn_cols += 1
            if columns == drawn_cols:
                str_cells_b += '┤'
            else:
                str_cells_b += '┼'
        return str_cells_b

    # code
    global board
    str_board = draw_top_border(n) + '\n'
    for i in range(0, n-1):
        str_board += draw_middle_border(n) + '\n'
        str_board += draw_cells_border(n) + '\n'
    str_board += draw_middle_border(n) + '\n'
    str_board += draw_bottom_border(n)
    board = str_board


def place_queen(queen_pos):
    """
    Place a queen in the chess board.
    :param queen_pos: tuple (i, j), where i is the x-coord and j is the y-coord. Notice that (0, 0) is the first position in the board.
    :return: a board with the queen placed in the position (i, j)
    """

    # code
    global board
    content_lines = list()
    new_board = ''
    lines = board.splitlines()
    for n in range(1, len(lines), 2):
        content_lines.append(lines[n])
    changed_line = content_lines[queen_pos[1]]
    xcoord = 0
    for c in range(1, len(changed_line)):
        if xcoord == queen_pos[0]:
            changed_line = changed_line[:c + 1] + "Q" + changed_line[c + 2:]
            break
        if changed_line[c] == '│':
            xcoord += 1
    content_lines[queen_pos[1]] = changed_line
    lines[1 + 2 * queen_pos[1]] = changed_line
    for n in range(0, len(lines)):
        new_board += lines[n] + '\n'
    board = new_board


def is_valid_board():
    """
    Return if is a valid board (no Queens placed in same row, column or diagonal).
    :return: Boolean True if the board is valid and False if the board is invalid.
    """

    # internal methods
    def transform_to_matrix(board):
        board_matrix = list(list())
        content_lines = list()
        lines = board.splitlines()
        for i in range(1, len(lines), 2):
            content_lines.append(lines[i])
        for i in range(0, len(content_lines)):
            aux_list = list()
            for j in range(0, len(content_lines)):
                aux_list.append(False)
            board_matrix.append(aux_list)
        for i in range(0, len(content_lines)):
            x_coord = 0
            for c in range(1, len(content_lines[i])):
                if content_lines[i][c] == 'Q':
                    board_matrix[i][x_coord] = True
                if content_lines[i][c] == '│':
                    x_coord += 1
        # print(board_matrix)
        return board_matrix

    def horizontal_test(board_matrix):
        horizontal_status = True
        for row in range(0, len(board_matrix)):
            num_true = 0
            for col in range(0, len(board_matrix[row])):
                if board_matrix[row][col]:
                    num_true += 1
                if num_true > 1:
                    horizontal_status = False
                    break
            if not horizontal_status:
                break
        # print(horizontal_status)
        return horizontal_status

    def vertical_test(board_matrix):
        vertical_status = True
        for col in range(0, len(board_matrix)):
            num_true = 0
            for row in range(0, len(board_matrix[col])):
                if board_matrix[row][col]:
                    num_true += 1
                if num_true > 1:
                    vertical_status = False
                    break
            if not vertical_status:
                break
        # print(vertical_status)
        return vertical_status

    def diagonal_test(board_matrix):
        diagonal_status = True
        board_order = len(board_matrix)
        diag_coords = list(list())
        aux_list = list()
        for i in range(1, 2*(board_order - 1)):
            for xcoord in range(0, board_order):
                for ycoord in range(0, board_order):
                    if xcoord + ycoord == i:
                        aux_list.append((xcoord, ycoord))
            diag_coords.append(aux_list.copy())
            aux_list.clear()
        for i in range(-(board_order - 2), board_order - 1):
            for xcoord in range(0, board_order):
                for ycoord in range(0, board_order):
                    if xcoord - ycoord == i:
                        aux_list.append((xcoord, ycoord))
            diag_coords.append(aux_list.copy())
            aux_list.clear()
        for i in range(0, len(diag_coords)):
            num_true = 0
            for j in range(0, len(diag_coords[i])):
                if board_matrix[diag_coords[i][j][0]][diag_coords[i][j][1]]:
                    num_true += 1
                if num_true > 1:
                    diagonal_status = False
                    break
            if not diagonal_status:
                break
        # print(diag_coords)
        return diagonal_status


    # code
    is_valid = False
    board_matrix = transform_to_matrix(board)
    if horizontal_test(board_matrix) and vertical_test(board_matrix) and diagonal_test(board_matrix):
        is_valid = True
    return is_valid


def print_board():
    """
    Print chess board with queens placed.
    :return: a unicode chess board with queens (Q) placed.
    """

    print(board.replace('┘\n', '┘'))
