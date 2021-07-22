from typing import List

class Solution:

    def _is_kink_on_the_right(self, lower_val, upper_val):
        return upper_val < lower_val

    def get_middle_idx(self, i_lower, i_upper):
        return i_lower + (i_upper - i_lower) // 2

    def search(self, nums: List[int], target: int) -> int:
        i_lower = 0
        i_upper = len(nums) - 1
        while (i_upper - i_lower) > 1:
            i_middle = self.get_middle_idx(i_lower, i_upper)
            middle_value = nums[i_middle]
            if target > middle_value:
                if self._is_kink_on_the_right(middle_value, nums[i_upper]):
                    i_lower = i_middle
                else:
                    if target > nums[i_upper]:
                        i_upper = i_middle
                    elif target < nums[i_upper]:
                        i_lower = i_middle
                    else:
                        return i_upper
            elif target < middle_value:
                if not self._is_kink_on_the_right(middle_value, nums[i_upper]):
                    i_upper = i_middle
                else:
                    if target > nums[i_lower]:
                        i_upper = i_middle
                    elif target < nums[i_lower]:
                        i_lower = i_middle
                    else:
                        return i_lower
            else:
                return i_middle

        for i in range(i_lower, i_upper+1):
            if nums[i] == target:
                return i
        return -1