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
            print(f'Median element dosr odd--> {median}')
            return median

        else:

            less_or_equal_hasnt_found = arr2_less_equal_ix == 0 and \
                                        self.arr2.arr[arr2_less_equal_ix] > self.arr1.arr[self.arr1.center]

            next_el_shift = 1

            if less_or_equal_hasnt_found:
                left_el = self.arr2.arr[arr2_less_equal_ix]

            else:
                left_el = self._check_center_pos()

            right_el = min(self.arr1.arr[self.arr1.center + next_el_shift],
                           self.arr2.arr[arr2_less_equal_ix + next_el_shift])

            median = (left_el + right_el) / 2
            print(f'Median element dosr even--> {median}')
            return median

    def one_array_logic(self, arr):

        median_ix = (len(arr) - 1) // 2
        if len(arr) % 2:
            return arr[median_ix]
        else:
            return 0.5 * (arr[median_ix] + arr[median_ix+1])

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

    def two_length_logic(self, has_searched):

        self.arr2.snapshot()
        arr2_less_equal_ix_left = self._find_balance_position(
            arr2=self.arr2,
            point=self.arr1.arr[0])
        self.arr2.restore()

        less_or_equal_hasnt_found = arr2_less_equal_ix_left == 0 and \
                                    self.arr2.arr[arr2_less_equal_ix_left] > self.arr1.arr[0]

        self.arr2.snapshot()
        arr2_less_equal_ix_right = self._find_balance_position(
            arr2=self.arr2,
            point=self.arr1.arr[1])
        self.arr2.restore()

        next_of_less_or_eq = int(not less_or_equal_hasnt_found)
        self.arr2.arr.insert(arr2_less_equal_ix_left + next_of_less_or_eq, self.arr1.arr[0])

        if arr2_less_equal_ix_right + 2 > len(self.arr2.arr) - 1:
            self.arr2.arr.append(self.arr1.arr[1])
        else:
            self.arr2.arr.insert(arr2_less_equal_ix_right + 2, self.arr1.arr[1])

        if not has_searched:
            return self.one_array_logic(self.arr2.arr)

        unification_ix_additive = 1
        unified_left_pointer = self.arr1.left_margin + self.arr2.left_margin + unification_ix_additive

        distance_to_median = self.median_position - unified_left_pointer

        if self.is_odd:
            return self.arr2.arr[self.arr2.left_margin + distance_to_median + 1]

        two_el_median = 0.5 * (self.arr2.arr[self.arr2.left_margin + distance_to_median + 1] +
                         self.arr2.arr[self.arr2.left_margin + distance_to_median + 2])
        return two_el_median

    def mergesort(self, arr1, arr2):
        print('mergesort')
        res_arr = []
        i, j = 0, 0
        while True:

            cur_min = min(arr1[i], arr2[j])

            if cur_min == arr1[i]:
                res_arr.append(cur_min)
                i += 1

            if cur_min == arr2[j]:
                res_arr.append(cur_min)
                j += 1

            if j >= len(arr2):
                if i < len(arr1):
                    res_arr.extend(arr1[i:])
                break

            if i >= len(arr1):
                if j < len(arr2):
                    res_arr.extend(arr2[j:])
                break

        assert len(res_arr) == len(arr1) + len(arr2)
        is_odd = len(res_arr) % 2
        median_position = (len(res_arr) - 1) // 2

        if is_odd:
            return res_arr[median_position]
        else:
            return 0.5 * (res_arr[median_position] + res_arr[median_position+1])

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

    def findMedianSortedArrays(self, nums1, nums2) -> float:

        if nums1 == []:
            return self.one_array_logic(nums2)

        if nums2 == []:
            return self.one_array_logic(nums1)

        if len(set(nums2) | set(nums1)) == 1:
            return nums1[0]

        if len(nums1 + nums2) <= 5:
            return self.mergesort(nums1, nums2)

        if len(nums2) < len(nums1):
            temp = nums2
            nums2 = nums1
            nums1 = temp

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


        if (len(self.arr1.arr) == 1) and (len(self.arr2.arr) == 1):
            return 0.5 * self.arr1.arr[0] + 0.5 * self.arr2.arr[0]

        if len(self.arr1.arr) == 1:
            return self.one_length_logic()

        if len(self.arr1.arr) == 2:
            return self.two_length_logic(has_searched=False)

        if self.arr1.right_margin - self.arr1.left_margin == 1:
            self.arr1.arr = [self.arr1.arr[self.arr1.left_margin],
                             self.arr1.arr[self.arr1.right_margin]]
            return self.two_length_logic(has_searched=True)




