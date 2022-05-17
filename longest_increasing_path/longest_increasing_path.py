import numpy as np

class Solution(object):

    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype:
        """
        if len(matrix) == 0:
            return 0
        self.matrix = np.array(matrix)
        self.weight_matrix = np.empty(self.matrix.shape)
        self.weight_matrix[:] = np.NaN
        self.action_list = ['left', 'right', 'up', 'bottom']
        self.sum_time = 0
        self._init_max()
        self._find()
        return int(self.weight_matrix.max())



    def _check_border(self, x_coord, y_coord):
        if (x_coord < self.matrix.shape[0]) & (x_coord >= 0) & (y_coord < self.matrix.shape[1]) & (y_coord >= 0):
            return True
        return False


    def _get_final_int(self, path_lst):
        return max([len(path.split("_")) for path in path_lst]) + 1


    def _init_max(self):
        max_mask = self.matrix == self.matrix.max()
        self.weight_matrix[max_mask] == 1


    def _make_step(self, x_new, y_new, x_coord, y_coord):
        if self._check_border(x_new, y_new,):
            if self.matrix[x_new, y_new] > self.matrix[x_coord, y_coord]:
                if np.isnan(self.weight_matrix[x_new, y_new]):
                    self._make_mooves(x_new, y_new)
                if self.weight_matrix[x_new, y_new] > self.weight_matrix[x_coord, y_coord]:
                    self.weight_matrix[x_coord, y_coord] = int(self.weight_matrix[x_new, y_new])


    def _make_mooves(self, x_coord, y_coord):
        if np.isnan(self.weight_matrix[x_coord, y_coord]):
            self.weight_matrix[x_coord, y_coord] = 0
            x_new = x_coord - 1
            self._make_step(x_new, y_coord, x_coord, y_coord)
            x_new = x_coord + 1
            self._make_step(x_new, y_coord, x_coord, y_coord)
            y_new = y_coord - 1
            self._make_step(x_coord, y_new, x_coord, y_coord)
            y_new = y_coord + 1
            self._make_step(x_coord, y_new, x_coord, y_coord)
            self.weight_matrix[x_coord, y_coord] += 1


    def _find(self):
        sorted_arr = np.dstack(np.unravel_index(np.argsort(-self.matrix.ravel()), self.matrix.shape))[0]
        for coord in sorted_arr:
            if np.isnan(self.weight_matrix[coord[0], coord[1]]):
                self._make_mooves(coord[0], coord[1])