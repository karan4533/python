class NQueens:
    def __init__(self, N):
        self.N = N
        self.solution_count = 0
        self.total_moves = 0

    def print_solution(self, board):
        self.solution_count += 1
        print("Solution", self.solution_count, ":")
        for i in range(self.N):
            for j in range(self.N):
                if board[i][j] == 1:
                    print(" Q ", end="")
                else:
                    print(" . ", end="")
            print()
        print()

    def is_safe(self, board, row, col):
        # Check if there's a queen in the same row
        for i in range(col):
            if board[row][i] == 1:
                return False

        # Check upper diagonal on left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        # Check lower diagonal on left side
        for i, j in zip(range(row, self.N), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        return True

    def solve_nq_util(self, board, col, moves):
        if col >= self.N:
            self.print_solution(board)
            self.total_moves += len(moves)
            print("Moves for Solution", self.solution_count, ":", len(moves))
            print()
            return True

        res = False
        for i in range(self.N):
            if self.is_safe(board, i, col):
                board[i][col] = 1
                moves.append((i, col))
                res = self.solve_nq_util(board, col + 1, moves) or res
                board[i][col] = 0
                moves.pop()

        return res

    def solve_nq(self):
        board = [[0] * self.N for _ in range(self.N)]

        if not self.solve_nq_util(board, 0, []):
            print("Solution does not exist")
            return False

        return True


def main():
    n_queens = NQueens(8)
    n_queens.solve_nq()
    print("Total solutions found:", n_queens.solution_count)
    print("Total moves made:", n_queens.total_moves)


if __name__ == "__main__":
    main()
