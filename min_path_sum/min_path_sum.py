from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        self.memo = [[0] * len(grid[0]) for _ in range(len(grid))]

        return self.dp(grid, 0, 0, 0)

    def dp(self, grid, i, j, path_sum):

        path_sum += grid[i][j]

        if self.memo[i][j] > 0:
            return path_sum + self.memo[i][j]

        if (i == len(grid) - 1) and (j == len(grid[0])-1):
            return path_sum

        elif i == len(grid)-1:
            whole_path = self.dp(grid, i, j+1, path_sum)

        elif j == len(grid[0])-1:
            whole_path = self.dp(grid, i+1, j, path_sum)

        else:
            whole_path = min(self.dp(grid, i+1, j, path_sum), self.dp(grid, i, j+1, path_sum))

        self.memo[i][j] = whole_path - path_sum

        return whole_path


grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
print(Solution().minPathSum(grid))



