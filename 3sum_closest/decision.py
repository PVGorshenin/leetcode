from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int):

        nums = sorted(nums)

        min_diff_sum = int(1e6)

        for i in range(len(nums)-2):
            j, k = i + 1, len(nums) - 1

            while j < k:
                curr_sum = nums[i] + nums[j] + nums[k]

                if abs(target - curr_sum) < (abs(target - min_diff_sum)):
                    min_diff_sum = curr_sum

                if curr_sum < target:
                    j += 1
                if curr_sum > target:
                    k -= 1
                if curr_sum == target:
                    return min_diff_sum

        return min_diff_sum


