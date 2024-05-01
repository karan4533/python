class NQueens:
    def __init__(self):
        self.N = 8
        self.min_solution_count = float('inf')
        self.solution_count = 0

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
        for i in range(col):
            if board[row][i] == 1:
                return False

        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        for i, j in zip(range(row, self.N), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        return True

    def solve_nq_util(self, board, col):
        if col >= self.N:
            self.print_solution(board)
            self.min_solution_count = min(self.min_solution_count, self.solution_count)
            return True

        res = False
        for i in range(self.N):
            if self.is_safe(board, i, col):
                board[i][col] = 1
                res = self.solve_nq_util(board, col + 1) or res
                board[i][col] = 0

        return res

    def solve_nq(self):
        board = [[0] * self.N for _ in range(self.N)]

        if not self.solve_nq_util(board, 0):
            print("Solution does not exist")
            return False

        print("Minimum number of solutions:", self.min_solution_count)
        return True


if __name__ == "__main__":
    queen = NQueens()
    queen.solve_nq()
