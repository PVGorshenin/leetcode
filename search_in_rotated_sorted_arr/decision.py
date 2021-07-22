class Solution:

    def _is_kink(self, lower_val, upper_val):
        return upper_val < lower_val

    def get_middle_idx(self, i_lower, i_upper):
        return (i_upper - i_lower) // 2

    def move_right(self, i_middle):
        i_lower = i_middle
        return i_lower

    def move_left(self, i_middle):
        i_upper = i_middle
        return i_upper

    def search(self, nums: List[int], target: int) -> int:
        i_lower = 0
        i_upper = len(nums)
        while (i_upper - i_lower) > 1:
            i_middle = self.get_middle_idx(i_upper, i_lower)
            middle_value = nums[i_middle]
            if target > middle_value:
                if self._is_kink(middle_value, nums[i_upper]):
                    i_lower = i_middle
                else:
                    if target > nums[i_upper]:
                        i_upper = i_middle
                    elif target < nums[i_upper]
                        i_lower = i_middle
                    else:
                        return i_upper
            elif target < middle_value:
                if self._is_kink(middle_value, nums[i_upper]):
                    i_lower = i_middle
                else:
                    i_upper = i_middle


