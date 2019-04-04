import contextlib
with contextlib.redirect_stdout(None):
    import pygame


def draw_board(queen_pos_board, n):

    '''
    Print a chessboard with the queens placed (GUI).
    :param queen_pos_board: position of the queens.
    :param n: board size (nxn) and number of queens.
    :return: void.
    '''

    pygame.init()
    pygame.display.set_caption(f'Solution for the {n}-Queens Problem')
    colors = [(255, 206, 158), (209, 139, 71)]      # orange and yellow
    # colors = [(236, 236, 210), (119, 149, 87)]    # dark and soft green

    board_size_px = 720     # board size (px)
    square_size = board_size_px // n
    board_size_px = n * square_size

    board = pygame.display.set_mode((board_size_px, board_size_px))

    queen_png = pygame.image.load("images/queen.png").convert_alpha()
    queen_png = pygame.transform.smoothscale(queen_png, (int(square_size*0.9), int(square_size*0.9)))

    queen_offset = (square_size-queen_png.get_width()) // 2

    while True:

        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            break;

        # draw a fresh chess board
        for row in range(n):        # draw each row of the board.
            c_index = row % 2       # alternate colors
            for col in range(n):
                square = (col*square_size, row*square_size, square_size, square_size)
                board.fill(colors[c_index], square)
                # flip the color index for the next square
                c_index = (c_index + 1) % 2

        # draw the queens.
        for (col, row) in enumerate(queen_pos_board):
          board.blit(queen_png,
                   (col*square_size+queen_offset,row*square_size+queen_offset))

        pygame.display.flip()


    pygame.quit()
