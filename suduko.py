def is_valid(board, row, col, num):
    # Check if num is already present in the row
    if num in board[row]:
        return False
    
    # Check if num is already present in the column
    for i in range(3):
        if board[i][col] == num:
            return False
    
    # Check if num is already present in the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    
    return True

def find_empty_location(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return (i, j)
    return None

def solve_sudoku(board):
    empty_location = find_empty_location(board)
    if not empty_location:
        return True
    
    row, col = empty_location
    
    for num in range(1, 4):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0  # Backtrack if the current configuration doesn't lead to a solution
    
    return False

def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

# Example Sudoku puzzle
puzzle = [
    [0, 0, 0],
    [0, 2, 0],
    [0, 0, 3]
]

if solve_sudoku(puzzle):
    print("Sudoku puzzle solved:")
    print_board(puzzle)
else:
    print("No solution exists for the given Sudoku puzzle.")
