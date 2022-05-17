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


matrix = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
          [19,18,17,16,15,14,13,12,11,10],
          [20,21,22,23,24,25,26,27,28,29],
          [39,38,37,36,35,34,33,32,31,30],
          [40,41,42,43,44,45,46,47,48,49],
          [59,58,57,56,55,54,53,52,51,50],
          [60,61,62,63,64,65,66,67,68,69],
          [79,78,77,76,75,74,73,72,71,70],
          [80,81,82,83,84,85,86,87,88,89],
          [99,98,97,96,95,94,93,92,91,90],
          [100,101,102,103,104,105,106,107,108,109],
          [119,118,117,116,115,114,113,112,111,110],
          [120,121,122,123,124,125,126,127,128,129],
          [139,138,137,136,135,134,133,132,131,130],
          [0,0,0,0,0,0,0,0,0,0]] * 100
print(Solution().longestIncreasingPath(matrix))