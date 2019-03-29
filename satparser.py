import pycryptosat


def solve_to_vars_assignment(solution):
    """
    Parse a solution (tuple) from solver() in cryptominisat for variable assignment (for looping purposes).
    :param solution: solver()[1] from cryptominisat.
    :return: variable assignment for iteration.
    """
    vars = list()
    for i in range(1, len(solution)):
        if not solution[i]:
            vars.append(int(i))
        else:
            vars.append(int(-i))
    return vars


def solve_to_queens_placement(solution):
    vars = list()
    for i in range(1, len(solution)+1):
        if not solution[i-1]:
            vars.append(int(-i))
        else:
            vars.append(int(i))
    return vars


def find_all_solutions(original_assignment):
    """
    Find all possible solution from a given CNF.
    :param original_assignment: input CNF.
    :return: list of SAT solutions from the input CNF.
    """
    solutions = list()
    solver = pycryptosat.Solver()
    for i in range(0, len(original_assignment)):
        solver.add_clause(original_assignment[i])
    while True:
        solver_solution = solver.solve()
        # print('Solution found!')
        if not solver_solution[0]:
            break
        solutions.append(solver_solution[1][1:])
        constraint_clauses = solve_to_vars_assignment(solver_solution[1])
        solver.add_clause(constraint_clauses)
    return solutions


def find_solution(original_assignment):
    """
    Find a valid solution (if it exists) from a given CNF.
    :param original_assignment: input CNF.
    :return: a tuple of a SAT solution from the input CNF.
    """
    solver = pycryptosat.Solver()
    for i in range(0, len(original_assignment)):
        solver.add_clause(original_assignment[i])
    solve_return = solver.solve()
    if not solve_return[1]:
        print('There is no valid solution.')
        exit(1)
    else:
        return solve_return[1][1:]