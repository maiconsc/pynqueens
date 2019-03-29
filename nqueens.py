import chessboard
import satparser


def horizontal_constraints(n):
    clauses = list(list())
    for y in range(1, n+1):
        for x in range(1, n+1):
            for i in range(x+1, n+1):
                aux = [-transform_coordinates_xy_to_val([x, y], n), -transform_coordinates_xy_to_val([i, y], n)]
                clauses.append(aux.copy())
    for y in range(1, n+1):
        aux = list()
        for x in range(1, n+1):
            aux.append(transform_coordinates_xy_to_val([x, y], n))
        clauses.append(aux)
    return clauses


def vertical_constraints(n):
    clauses = list(list())
    for x in range(1, n+1):
        for y in range(1, n+1):
            for i in range(y+1, n+1):
                aux = [-transform_coordinates_xy_to_val([x, y], n), -transform_coordinates_xy_to_val([x, i], n)]
                clauses.append(aux.copy())
    for x in range(1, n+1):
        aux = list()
        for y in range(1, n+1):
            aux.append(transform_coordinates_xy_to_val([x, y], n))
        clauses.append(aux)
    return clauses


def diagonal_constraints(n):

    # internal method
    def compute_diagonal(i, n, type):
        di = list(list())
        possible_x = list()
        possible_y = list()
        for j in range(0, n):
            possible_x.append(j)
            possible_y.append(j)
        if type == 'anti':
            for j in range(0, len(possible_x)):
                for k in range(0, len(possible_y)):
                    if (possible_x[j] + possible_y[k]) == i:
                        di.append([possible_x[j]+1, possible_y[k]+1])
        elif type == 'main':
            for j in range(0, len(possible_x)):
                for k in range(0, len(possible_y)):
                    if (possible_x[j] - possible_y[k]) == i:
                        di.append([possible_x[j]+1, possible_y[k]+1])
        return di

    # code
    clauses = list(list())
    for i in range(1, 2*n-2):
        d = compute_diagonal(i, n, 'anti')
        for j in range(1, len(d) + 1):
            for k in range(j+1, len(d)+1):
                aux = [-transform_coordinates_xy_to_val(d[j-1], n), -transform_coordinates_xy_to_val(d[k-1], n)]
                clauses.append(aux.copy())
        aux = list()
    for i in range(-n+2, n-1):
        d = compute_diagonal(i, n, 'main')
        for j in range(1, len(d) + 1):
            for k in range(j+1, len(d)+1):
                aux = [-transform_coordinates_xy_to_val(d[j-1], n), -transform_coordinates_xy_to_val(d[k-1], n)]
                clauses.append(aux.copy())
        aux = list()
    return clauses


def transform_coordinates_xy_to_val(coord_xy, n):
    return (coord_xy[1] - 1)*n + coord_xy[0]


def transform_coordinates_val_to_xy(val, n):
    xy_tuple = ((val-1) % n, int((val - 1)/n))
    return xy_tuple


def main():
    print('------- N-QUEENS -- SAT MODELLING -------')
    n = int(input('- Enter N: '))
    mode = str(input('-- Enter A/a for all solutions or o/O for one solution: ')).lower()[0]

    original_assignment = list()

    # creation of clauses for horizontal constraints
    horizontal_clauses = horizontal_constraints(n)
    for i in range(0, len(horizontal_clauses)):
        original_assignment.append(horizontal_clauses[i])

    # creation of clauses for vertical constraints
    vertical_clauses = vertical_constraints(n)
    for i in range(0, len(vertical_clauses)):
        original_assignment.append(vertical_clauses[i])

    # creation of clauses for diagonal constraints
    diagonal_clauses = diagonal_constraints(n)
    for i in range(0, len(diagonal_clauses)):
        original_assignment.append(diagonal_clauses[i])

    if mode == 'o':
        chessboard.create_board(n)
        solution = satparser.find_solution(original_assignment)
        pos_queens_val = satparser.solve_to_queens_placement(solution)
        for i in range(0, len(pos_queens_val)):
            if pos_queens_val[i] > 0:
                chessboard.place_queen(transform_coordinates_val_to_xy(pos_queens_val[i], n))
        chessboard.print_board()
    elif mode == 'a':
        solutions = satparser.find_all_solutions(original_assignment)
        while True:
            mode_multiple = int(input(f'--- Number of solutions found: {len(solutions)}. \n--- Enter the id of the '
                                      f'solution (1 to {len(solutions)}) to show it, 0 to see all the valid boards or '
                                      f'a negative value to exit: '))
            if mode_multiple < 0:
                break
            elif mode_multiple == 0:
                for k in range(0, len(solutions)):
                    chessboard.create_board(n)
                    pos_queens_val = satparser.solve_to_queens_placement(solutions[k])
                    for i in range(0, len(pos_queens_val)):
                        if pos_queens_val[i] > 0:
                            chessboard.place_queen(transform_coordinates_val_to_xy(pos_queens_val[i], n))
                    print(f'\nSolution #{k + 1}:')
                    chessboard.print_board()
            elif 0 < mode_multiple <= len(solutions):
                chessboard.create_board(n)
                pos_queens_val = satparser.solve_to_queens_placement(solutions[mode_multiple - 1])
                for i in range(0, len(pos_queens_val)):
                    if pos_queens_val[i] > 0:
                        chessboard.place_queen(transform_coordinates_val_to_xy(pos_queens_val[i], n))
                print(f'\nSolution #{mode_multiple}:')
                chessboard.print_board()
            print(50*'-')


if __name__ == "__main__":
    main()
