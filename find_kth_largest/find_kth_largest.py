from typing import List


def binary_search(lst, val):
    left_ix, right_ix = 0, len(lst) - 1

    while right_ix - left_ix > 1:
        mid_ix = left_ix + (right_ix - left_ix) // 2

        if val > lst[mid_ix]:
            left_ix = mid_ix
        elif val < lst[mid_ix]:
            right_ix = mid_ix
        else:
            return mid_ix

    if val > lst[right_ix]:
        return right_ix

    return left_ix


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        to_reflect_around_zero = 1

        if k > (len(nums)) // 2:
            nums = [-1 * num for num in nums]
            to_reflect_around_zero = -1

            k = len(nums) - k + 1

        candidate_lst = [nums[0]]
        min_el_value, max_el_value = nums[0], nums[0]
        nums.pop(0)
        better_not_sort = 3

        while k:

            i_num = 0
            while i_num < len(nums):

                num = nums[i_num]

                if num >= min_el_value:

                    if len(candidate_lst) > better_not_sort:
                        less_or_eq_ix = binary_search(candidate_lst, num)
                        candidate_lst.insert(less_or_eq_ix + 1, num)

                    else:
                        candidate_lst.append(num)
                        candidate_lst = sorted(candidate_lst)

                    if len(candidate_lst) > k:
                        candidate_lst = candidate_lst[1:]

                    min_el_value = candidate_lst[0]

                    nums.pop(i_num)

                else:
                    i_num += 1

            if len(candidate_lst) == k:
                return candidate_lst[0] * to_reflect_around_zero

            else:
                k -= len(candidate_lst)
                candidate_lst = [nums[0]]
                min_el_value = nums[0]
                nums.pop(0)

        return None



