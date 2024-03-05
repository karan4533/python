def is_valid(grid, row, col, num):
    # Check if the number is already present in the row or column
    for i in range(3):
        for j in range(3):
            if grid[row * 3 + i][col * 3 + j] == num:
                return False
    return True

def solve_sudoku(grid, row, col):
    if row == 3 and col == 0:
        return True

    next_row = row + (col + 1) // 3
    next_col = (col + 1) % 3

    for num in range(1, 10):
        if is_valid(grid, row, col, num):
            grid[row * 3 + (col // 3)][col * 3 + (col % 3)] = num
            if solve_sudoku(grid, next_row, next_col):
                return True
            grid[row * 3 + (col // 3)][col * 3 + (col % 3)] = 0

    return False

def print_sudoku(grid):
    for i in range(3):
        if i > 0 and i % 3 == 0:
            print("- - - - - - - - - - -")
        for j in range(3):
            if j > 0 and j % 3 == 0:
                print("|", end=" ")
            print(grid[i][j], end=" ")
        print()

# Example initial puzzle (0 means empty cell)
initial_grid = [
    [0, 0, 3],
    [2, 0, 0],
    [0, 1, 0]
]

# Solve the puzzle
if solve_sudoku(initial_grid, 0, 0):
    print("Sudoku solution:")
    print_sudoku(initial_grid)
else:
    print("No solution found.")
