from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]):
        self.res_dct = {}

        for i_row in range(len(matrix)):
            for i_col in range(len(matrix[0])):
                key = f'{i_row},{i_col}'
                if key not in self.res_dct:
                    self._find_bigger_neighbours(matrix, i_row, i_col)

        return max(self.res_dct.values())

    def _find_bigger_neighbours(self, matrix,  i_row, i_col):
        max_len = 0
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        key = f'{i_row},{i_col}'

        if i_row == 0: moves.remove((-1, 0))
        if i_row == len(matrix)-1: moves.remove((1, 0))
        if i_col == 0: moves.remove((0, -1))
        if i_col == len(matrix[0])-1: moves.remove((0, 1))

        for move in moves:
            row_shift, col_shift = move

            if matrix[i_row+row_shift][i_col+col_shift] > matrix[i_row][i_col]:
                curr_key = f'{i_row+row_shift},{i_col+col_shift}'

                if curr_key in self.res_dct:
                    curr_len = self.res_dct[curr_key]

                else:
                    curr_len = self._find_bigger_neighbours(matrix, i_row+row_shift, i_col+col_shift)
                max_len = max(curr_len, max_len)

        max_len += 1
        self.res_dct[key] = max_len
        return max_len



