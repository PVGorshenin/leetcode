from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        self.global_max = 0
        self.memo = {}

        if len(nums) <= 2:
            return max(nums)

        for i in range(0, 2):
            curr_sum = nums[i]
            dfs_sum = self.dfs(nums, i+2, curr_sum)

            if dfs_sum > self.global_max:
                self.global_max = dfs_sum

        return self.global_max


    def dfs(self, nums, i, prev_sum):

        if i >= len(nums):
            return prev_sum

        max_sum = prev_sum

        for j in range(i, len(nums)):

            curr_sum = prev_sum + nums[j]

            if j in self.memo.keys():
                dfs_sum = self.memo[j] + curr_sum
            else:
                dfs_sum = self.dfs(nums, j+2, curr_sum)
                self.memo[j] = dfs_sum - curr_sum

            if dfs_sum > max_sum:
                max_sum = dfs_sum

        return max_sum




nums = [104,209,137,52,158,67,213,86,141,110,151,127,238,147,169,138,240,185,246,225,147,203,83,83,131,227,54,78,165,180,214,151,111,161,233,147,124,143]
print(Solution().rob(nums))




