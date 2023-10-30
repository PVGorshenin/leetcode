from typing import List


class Solution:

    def dfs(self, board, i, j):
        is_beyond_border = ((i == self.n_rows) | (j == self.n_cols) | \
                            (i == -1) | (j == -1))

        if is_beyond_border:
            return None

        is_seen_or_x = (board[i][j] == 'X') | (board[i][j] == '#')

        if is_seen_or_x:
            return None

        board[i][j] = '#'

        self.dfs(board, i + 1, j)
        self.dfs(board, i - 1, j)
        self.dfs(board, i, j - 1)
        self.dfs(board, i, j + 1)


    def solve(self, board: List[List[str]]) -> None:

        self.n_rows = len(board)
        self.n_cols = len(board[0])

        for i in range(self.n_rows):
            for j in [0, self.n_cols-1]:
                if board[i][j] == 'O':
                    self.dfs(board, i, j)

        for j in range(1, self.n_cols-1):
            for i in [0, self.n_rows-1]:
                if board[i][j] == 'O':
                    self.dfs(board, i, j)

        for i in range(self.n_rows):
            for j in range(self.n_cols):
                if board[i][j] == '#':
                    board[i][j] = 'O'

                elif board[i][j] == 'O':
                    board[i][j] = 'X'

        return board




a = [
    ["O", "X", "X", "O", "X"],
    ["X", "O", "O", "X", "O"],
    ["X", "O", "X", "O", "X"],
    ["O", "X", "O", "O", "O"],
    ["X", "X", "O", "X", "O"]
]

for row in Solution().solve(a):
    print(row)
