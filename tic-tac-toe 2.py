EMPTY = '-'  # Represents an empty cell
X = 'X'      # Represents a cell with 'X'
O = 'O'      # Represents a cell with 'O'

def generate_possibilities(board, row, col):
    # Check if the entire board has been filled
    if row == 3:
        display_board(board)
        return

    # Iterate through each symbol: 'X', 'O', and '-'
    for i in range(3):
        # Set the current cell to the corresponding symbol
        board[row][col] = EMPTY if i == 0 else (X if i == 1 else O)
        
        # Move to the next cell in the same row
        if col < 2:
            generate_possibilities(board, row, col + 1)
        # Move to the first cell of the next row
        else:
            generate_possibilities(board, row + 1, 0)

def display_board(board):
    # Print the current state of the board
    for row in board:
        print(' '.join(row))
    print("---------")

if __name__ == "__main__":
    # Initialize an empty 3x3 board
    board = [['' for _ in range(3)] for _ in range(3)]
    
    # Generate all possible board configurations
    generate_possibilities(board, 0, 0)
