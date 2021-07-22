from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n_jumps, i = 0, 0
        if len(nums) == 1:
            return 0
        if i + nums[i] >= len(nums) - 1:
            return 1
        while i < len(nums):
            n_candidates = nums[i]
            curr_max_2step_jump = 0
            curr_maxjump_idx = i
            for offset in range(1, n_candidates+1):
                curr_jump = offset + nums[i+offset]
                if curr_jump > curr_max_2step_jump:
                    curr_max_2step_jump = curr_jump
                    curr_maxjump_idx = i + offset
            n_jumps += 1
            i = curr_maxjump_idx
            if i >= len(nums) - 1:
                return n_jumps
            if i + nums[i] >= len(nums) - 1:
                return n_jumps + 1



