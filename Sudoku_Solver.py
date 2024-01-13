from constraint import Problem

def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))

def solve_sudoku(grid):
    problem = Problem()

    # Define the variables (cells) and their possible values (1-9)
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                problem.addVariable((i, j), range(1, 10))

    # Define the constraints (rows, columns, and 3x3 subgrids)
    for i in range(9):
        problem.addConstraint(lambda *values: len(set(values)) == len(values), [(i, j) for j in range(9)])
        problem.addConstraint(lambda *values: len(set(values)) == len(values), [(j, i) for j in range(9)])

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            problem.addConstraint(lambda a, b, c, d, e, f, g, h, i: len(set([a, b, c, d, e, f, g, h, i])) == 9,
                                  [(i + x, j + y) for x in range(3) for y in range(3)])

    # Solve the Sudoku puzzle using backtracking
    solution = problem.getSolution()

    if solution:
        for (i, j), value in solution.items():
            grid[i][j] = value

        return True
    else:
        return False

# Function to get user input for Sudoku puzzle
def get_user_input():
    sudoku_grid = []
    print("Enter the Sudoku puzzle row by row. Use '0' for empty cells.")

    for _ in range(9):
        row = input("Enter a row (9 numbers separated by spaces): ")
        sudoku_grid.append(list(map(int, row.split())))

    return sudoku_grid

# Get user input for Sudoku puzzle
user_input_grid = get_user_input()

print("\nEntered Sudoku Puzzle:")
print_grid(user_input_grid)
print("\nSolving...\n")

# Solve the Sudoku puzzle
if solve_sudoku(user_input_grid):
    print("Sudoku Solved:")
    print_grid(user_input_grid)
else:
    print("No solution exists.")

