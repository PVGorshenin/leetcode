from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n_jumps, i_number = 0, 0
        if len(nums) == 1:
            return 0

        if i_number + nums[i_number] >= len(nums) - 1:
            return 1

        while i_number < len(nums):
            n_candidates = nums[i_number]
            curr_max_2step_jump = 0
            curr_maxjump_idx = i_number

            for offset in range(1, n_candidates+1):
                curr_jump = offset + nums[i_number+offset]
                if curr_jump > curr_max_2step_jump:
                    curr_max_2step_jump = curr_jump
                    curr_maxjump_idx = i_number + offset

            n_jumps += 1
            i_number = curr_maxjump_idx
            if i_number >= len(nums) - 1:
                return n_jumps

            if i_number + nums[i_number] >= len(nums) - 1:
                return n_jumps + 1



