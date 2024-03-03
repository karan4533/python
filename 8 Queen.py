N = 8  # (size of the chessboard)
solutions_found = 0  # Variable to track the number of solutions found

def solveNQueens(board, col, solutions):
    global solutions_found
    if solutions_found == 5:  # Stop when 5 solutions are found
        return
    if col == N:
        solutions.append([row[:] for row in board])  # Copy the board to solutions
        solutions_found += 1
        return
    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1
            solveNQueens(board, col + 1, solutions)
            board[i][col] = 0

def isSafe(board, row, col):
    for x in range(col):
        if board[row][x] == 1:
            return False
    for x, y in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[x][y] == 1:
            return False
    for x, y in zip(range(row, N, 1), range(col, -1, -1)):
        if board[x][y] == 1:
            return False
    return True

def print_board(board):
    for i in range(N):
        for j in range(N):
            print(board[j][i], end=" ")
        print()

solutions = []
board = [[0 for x in range(N)] for y in range(N)]
solveNQueens(board, 0, solutions)

if solutions_found > 0:
    print("5 Solutions found:")
    for idx, solution in enumerate(solutions[:5]):
        print(f"Solution {idx + 1}:")
        print_board(solution)
        print()
else:
    print("No solution found")
