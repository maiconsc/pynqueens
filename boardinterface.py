import contextlib
with contextlib.redirect_stdout(None):
    import pygame


def draw_board(the_board, n):
    """ Draw a chess board with queens, as determined by the the_board. """

    pygame.init()
    pygame.display.set_caption(f'Solution for the {n}-Queens Problem')
    colors = [(209, 139, 71), (255, 206, 158)]    # Set up colors [red, black]

    n = len(the_board)         # This is an NxN chess board.
    surface_sz = 720           # Proposed physical surface size.
    sq_sz = surface_sz // n    # sq_sz is length of a square.
    surface_sz = n * sq_sz     # Adjust to exactly fit n squares.

    # Create the surface of (width, height), and its window.
    surface = pygame.display.set_mode((surface_sz, surface_sz))

    BLACK = (0, 0, 0)
    ball = pygame.image.load("images/queen.png").convert_alpha()
    ball = pygame.transform.smoothscale(ball, (int(sq_sz*0.9), int(sq_sz*0.9)))


    # Use an extra offset to centre the ball in its square.
    # If the square is too small, offset becomes negative,
    #   but it will still be centered 🙂
    ball_offset = (sq_sz-ball.get_width()) // 2

    while True:

        # Look for an event from keyboard, mouse, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break;

        # Draw a fresh background (a blank chess board)
        for row in range(n):           # Draw each row of the board.
            c_indx = row % 2           # Alternate starting color
            for col in range(n):       # Run through cols drawing squares
                the_square = (col*sq_sz, row*sq_sz, sq_sz, sq_sz)
                surface.fill(colors[c_indx], the_square)
                # Now flip the color index for the next square
                c_indx = (c_indx + 1) % 2

        # Now that squares are drawn, draw the queens.
        for (col, row) in enumerate(the_board):
          surface.blit(ball,
                   (col*sq_sz+ball_offset,row*sq_sz+ball_offset))

        pygame.display.flip()


    pygame.quit()