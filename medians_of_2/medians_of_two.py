import numpy as np


class Array():
    def __init__(self, arr):
        self.arr = arr
        self.left_margin = 0
        self.right_margin = len(arr) - 1
        self.center = (len(arr) - 1) // 2

    def snapshot(self):
        self.left_margin_ = self.left_margin
        self.right_margin_ = self.right_margin
        self.center_ = self.center

    def restore(self):
        self.left_margin = self.left_margin_
        self.right_margin = self.right_margin_
        self.center = self.center_


class Solution():

    def _get_center(self, arr):
        shift = (arr.right_margin - arr.left_margin) // 2
        return arr.left_margin + shift

    def _go_left(self, arr):
        arr.right_margin = arr.center
        arr.center = self._get_center(arr)

    def _go_right(self, arr):
        arr.left_margin = arr.center
        arr.center = self._get_center(arr)

    def _go_left_to_point(self, arr, point):
        arr.right_margin = point
        arr.center = self._get_center(arr)

    def _go_right_to_point(self, arr, point):
        arr.left_margin = point
        arr.center = self._get_center(arr)

    def _check_center_pos(self):
        return self.arr1.arr[self.arr1.center]

    def _find_balance_position(self, arr2, point):
        '''
        Finds closet less

        #TODO: добавить границы при равенстве элементов
        '''
        while (arr2.right_margin - arr2.left_margin) > 1:

            if arr2.arr[arr2.center] == point:
                return arr2.center

            if arr2.arr[arr2.center] > point:
                self._go_left(arr2)
            else:
                self._go_right(arr2)

        if arr2.arr[arr2.right_margin] <= point:
            return arr2.right_margin

        return arr2.left_margin

    def _move_borders(self, balance_point, arr2_less_equal_ix):

        if balance_point > self.median_position:
            self._go_left(self.arr1)
            self._go_left_to_point(self.arr2, arr2_less_equal_ix)

        elif balance_point < self.median_position:
            self._go_right(self.arr1)
            self._go_right_to_point(self.arr2, arr2_less_equal_ix)

    def _median_found(self, arr2_less_equal_ix):

        if self.is_odd:
            median = self._check_center_pos()
            print(f'Median element dosr1--> {median}')
            return median

        else:
            left_el = self._check_center_pos()
            next_el_shift = 1

            right_el = min(self.arr1.arr[self.arr1.center + next_el_shift],
                           self.arr2.arr[arr2_less_equal_ix + next_el_shift])
            median = (left_el + right_el) / 2
            print(f'Median element dosr2--> {median}')
            return median

    def one_length_logic(self):

        x = self.arr1.arr[0]
        if self.is_odd:
            is_in_the_middle = x >= self.arr2.arr[self.arr2.center] and \
                               x <= self.arr2.arr[self.arr2.center + 1]
            if is_in_the_middle:
                return x
            elif x > self.arr2.arr[self.arr2.center]:
                return self.arr2.arr[self.arr2.center + 1]

            return self.arr2.arr[self.arr2.center]

        else:
            is_left_from_arr2_median = self.arr2.arr[self.arr2.center - 1] <= x <= self.arr2.arr[self.arr2.center]
            is_right_from_arr2_median = self.arr2.arr[self.arr2.center] <= x <= self.arr2.arr[self.arr2.center + 1]

            is_less_arr2_median = x < self.arr2.arr[self.arr2.center]
            is_more_arr2_median = x > self.arr2.arr[self.arr2.center]

            if is_left_from_arr2_median or is_right_from_arr2_median:
                return 0.5 * (x + self.arr2.arr[self.arr2.center])
            elif is_less_arr2_median:
                return 0.5 * (self.arr2.arr[self.arr2.center - 1] + self.arr2.arr[self.arr2.center])
            elif is_more_arr2_median:
                return 0.5 * (self.arr2.arr[self.arr2.center] + self.arr2.arr[self.arr2.center + 1])

    def two_length_logic(self):

        unification_ix_additive = 1

        self.arr1.center = 1

        self.arr2.snapshot()
        arr2_less_equal_ix = self._find_balance_position(
            arr2=self.arr2,
            point=self.arr1.arr[self.arr1.center])
        self.arr2.restore()

        balance_point = 1 + arr2_less_equal_ix + unification_ix_additive

        if balance_point != self.median_position:
            self._move_borders(
                balance_point=balance_point,
                arr2_less_equal_ix=arr2_less_equal_ix
            )

        else:
            return self._median_found(arr2_less_equal_ix)

    def three_length_logic(self):
        if self.arr2.arr[0] <= self.arr1.arr[0] <= self.arr2.arr[1]:
            return self.arr1.arr[0]
        if self.arr1.arr[0] >= self.arr2.arr[1]:
            return self.arr2.arr[1]
        return self.arr2.arr[0]

    def _unintersect_script(self, arr1, arr2):

        if arr1.right_margin >= self.median_position:
            left_el = arr1.arr[self.median_position]

            if not self.is_odd:

                if arr1.right_margin >= (self.median_position + 1):
                    right_el = arr1.arr[self.median_position + 1]
                else:
                    right_el = arr2.arr[0]
                median = .5 * (left_el + right_el)
                print(f'Median element uninter1--> {median}')
                return median

            print(f'Median element uninter1--> {left_el}')
            return left_el
        else:
            shift = self.median_position - arr1.right_margin - 1
            left_el = arr2.arr[shift]

            if not self.is_odd:
                right_el = arr2.arr[shift + 1]
                median = .5 * (left_el + right_el)
                print(f'Median element uninter1--> {median}')
                return median

            print(f'Median element uninter--> {left_el}')
            return left_el

    def _final_chunk_odd_logic(self, left_pointer, right_pointer):

        if (left_pointer < self.median_position) & (right_pointer > self.median_position):
            shift = self.median_position - left_pointer
            return self.arr2.arr[self.arr2.left_margin + shift]

        elif left_pointer > self.median_position:
            return self.arr2.arr[self.median_position]

        elif right_pointer < self.median_position:
            return self.arr2.arr[self.median_position - len(self.arr1.arr)]

    def _final_chunk_pass(self, left_pointer, right_pointer):

        if self.is_odd:
            return self._final_chunk_odd_logic(left_pointer, right_pointer)

        else:
            left_el = self._final_chunk_odd_logic(left_pointer, right_pointer)
            next_el_shift = 1
            self.median_position += next_el_shift

            if right_pointer == self.median_position:
                right_el = self.arr1.arr[self.arr1.right_margin]
            else:
                right_el = self._final_chunk_odd_logic(left_pointer, right_pointer)
            return (left_el + right_el) / 2

    def findMedianSortedArrays(self, nums1, nums2) -> float:

        self.arr1 = Array(nums1)
        self.arr2 = Array(nums2)

        self.is_odd = (len(nums1) + len(nums2)) % 2
        self.median_position = (len(self.arr1.arr) + len(self.arr2.arr) - 1) // 2
        unification_ix_additive = 1

        if self.arr1.arr[-1] < self.arr2.arr[0]:
            median = self._unintersect_script(self.arr1, self.arr2)
            return median
        if self.arr2.arr[-1] < self.arr1.arr[0]:
            median = self._unintersect_script(self.arr2, self.arr1)
            return median

        index_distance_first_arr = self.arr1.right_margin - self.arr1.left_margin

        while index_distance_first_arr > 1:

            self.arr2.snapshot()
            arr2_less_equal_ix = self._find_balance_position(
                arr2=self.arr2,
                point=self.arr1.arr[self.arr1.center])
            self.arr2.restore()

            balance_point = self.arr1.center + arr2_less_equal_ix + unification_ix_additive

            if balance_point != self.median_position:
                self._move_borders(
                    balance_point=balance_point,
                    arr2_less_equal_ix=arr2_less_equal_ix
                )

            else:
                return self._median_found(arr2_less_equal_ix)

            index_distance_first_arr = self.arr1.right_margin - self.arr1.left_margin
            print(index_distance_first_arr)

        if (len(self.arr1.arr) == 1) and (len(self.arr2.arr) == 1):
            return 0.5 * self.arr1.arr[0] + 0.5 * self.arr2.arr[0]

        if (len(self.arr1.arr) == 1) and (len(self.arr2.arr) == 2):
            return self.three_length_logic()

        if (len(self.arr1.arr) == 2) and (len(self.arr2.arr) == 1):
            tmp = self.arr2.arr
            self.arr2.arr = self.arr1.arr
            self.arr1.arr = tmp
            return self.three_length_logic()

        if len(self.arr1.arr) == 1:
            return self.one_length_logic()

        if len(self.arr1.arr) == 2:
            return self.two_length_logic()

        united_left_pointer = self.arr1.left_margin + self.arr2.left_margin + unification_ix_additive
        united_right_pointer = self.arr1.right_margin + self.arr2.right_margin + unification_ix_additive

        median_el = self._final_chunk_pass(united_left_pointer, united_right_pointer)
        print(f'Median element--> {median_el}')

        return median_el

a = [1, 3]
b = [2]
print(Solution().findMedianSortedArrays(a, b))

def find_median(a, b):
    print()
    print('np median -->', np.median(a+b))
    print(sorted(a+b))

find_median(a, b)





