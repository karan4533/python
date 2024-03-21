import random

def generate_tic_tac_toe_solutions():
    solutions = []

    # Possible winning combinations
    winning_combos = [
        ["X", "X", "X", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "X", "X", "X", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "X", "X", "X"],
        ["X", "-", "-", "X", "-", "-", "X", "-", "-"],
        ["-", "X", "-", "-", "X", "-", "-", "X", "-"],
        ["-", "-", "X", "-", "-", "X", "-", "-", "X"],
        ["X", "-", "-", "-", "X", "-", "-", "-", "X"],
        ["-", "-", "X", "-", "X", "-", "X", "-", "-"]
    ]

    # Shuffle the winning combinations to randomize the order
    random.shuffle(winning_combos)

    # Add the first 15 combinations to the solutions list
    for i in range(min(15, len(winning_combos))):
        solutions.append(winning_combos[i])

    return solutions

def print_board(board):
    print("|---|---|---|")
    for i in range(0, 9, 3):
        print("| " + " | ".join(board[i:i+3]) + " |")
        print("|---|---|---|")

if __name__ == "__main__":
    # Generate 15 possible solutions
    solutions = generate_tic_tac_toe_solutions()

    # Print the solutions
    print("8 Possible Solutions for Tic Tac Toe:")
    for i, solution in enumerate(solutions):
        print("Solution " + str(i + 1) + ":")
        print_board(solution)
        print()
