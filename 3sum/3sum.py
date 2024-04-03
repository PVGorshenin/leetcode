from typing import List
from time import time


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)

        res_set = set()
        for i in range(len(nums)-2):

            j = i + 1
            k = len(nums) - 1

            three_first_sum = nums[i] + nums[j] + nums[j+1]

            if three_first_sum > 0:
                return res_set

            three_last_sum = nums[k] + nums[k-1] + nums[k-2]
            if three_last_sum < 0:
                return res_set

            while j < k:

                curr_sum = nums[i] + nums[j] + nums[k]
                if curr_sum == 0:
                    curr_combination = (nums[i], nums[j], nums[k])
                    if curr_combination not in res_set:
                        res_set.add(curr_combination)

                    k -= 1
                    j += 1

                elif curr_sum > 0:
                    k -= 1

                else:
                    j += 1

        return res_set


