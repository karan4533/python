M = 9  # Size of the puzzle

def puzzle(a):
    for i in range(M):
        for j in range(M):
            print(a[i][j], end=" ")
            if (j + 1) % 3 == 0 and j != M - 1:
                print("|", end=" ")
        print()
        if (i + 1) % 3 == 0 and i != M - 1:
            print("- " * (M + 2))

def solve(grid, row, col, num):
    for x in range(M):
        if grid[row][x] == num:
            return False
    
    for x in range(M):
        if grid[x][col] == num:
            return False

    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True

def Sudoku(grid, row, col):
    if (row == M - 1 and col == M):
        return True
    if col == M:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return Sudoku(grid, row, col + 1)
    for num in range(1, M + 1, 1): 
        if solve(grid, row, col, num):
            grid[row][col] = num
            if Sudoku(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False

# 3x3 Sudoku puzzle grid (0 means the cells where no value is assigned)
grid = [[2, 5, 0, 0, 3, 0, 9, 0, 1],
        [0, 1, 0, 0, 0, 4, 0, 0, 0],
        [4, 0, 7, 0, 0, 0, 2, 0, 8],
        [0, 0, 5, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 8, 1, 0, 0],
        [0, 4, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 3, 6, 0, 0, 7, 2],
        [0, 7, 0, 0, 0, 0, 0, 0, 3],
        [9, 0, 3, 0, 0, 0, 6, 0, 4]]

if Sudoku(grid, 0, 0):
    puzzle(grid)
else:
    print("Solution does not exist :(")
