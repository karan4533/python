def print_board(board):
    for i in range(1, 10, 3):
        print("|", end=" ")
        for j in range(3):
            print(board[i + j - 1], end=" | ")
        print("\n" + "-" * 13)

def make_move(board, player):
    while True:
        try:
            position = int(input(f"Player {player}, enter position (1-9): "))
            if 1 <= position <= 9 and board[position - 1] == ' ':
                board[position - 1] = player
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def check_winner(board):
    for i in range(1, 10, 3):
        if board[i - 1] != ' ' and board[i - 1] == board[i] == board[i + 1]:
            return True
    for i in range(1, 4):
        if board[i - 1] != ' ' and board[i - 1] == board[i + 2] == board[i + 5]:
            return True
    if board[0] != ' ' and board[0] == board[4] == board[8]:
        return True
    if board[2] != ' ' and board[2] == board[4] == board[6]:
        return True
    return False

def is_board_full(board):
    return all(cell != ' ' for cell in board)

def tic_tac_toe():
    board = [' ' for _ in range(9)]
    current_player = 'X'

    while True:
        print_board(board)
        make_move(board, current_player)

        if check_winner(board):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("The game is a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe()
