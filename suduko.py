SIZE = 3

def main():
    board = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
    display_possibilities(board, 0, 0)

def display_possibilities(board, row, col):
    if row == SIZE:
        display_board(board)
        return

    for num in range(1, SIZE+1):
        if is_valid(board, row, col, num):
            board[row][col] = num
            next_row = row
            next_col = col + 1
            if next_col == SIZE:
                next_row += 1
                next_col = 0
            display_possibilities(board, next_row, next_col)
            board[row][col] = 0

def is_valid(board, row, col, num):
    for i in range(SIZE):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row = row - row % (SIZE // 3)
    start_col = col - col % (SIZE // 3)
    for i in range(SIZE // 3):
        for j in range(SIZE // 3):
            if board[i + start_row][j + start_col] == num:
                return False

    return True

def display_board(board):
    for i in range(SIZE):
        for j in range(SIZE):
            print(board[i][j], end=" ")
        print()
    print()

if __name__ == "__main__":
    main()
