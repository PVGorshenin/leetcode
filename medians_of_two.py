import numpy as np

class Array():
    def __init__(self, arr):
        self.arr = arr
        self.left_margin = 0
        self.right_margin = len(arr)-1
        self.center = len(arr) // 2

    def snapshot(self):
        self.left_margin_ = self.left_margin
        self.right_margin_ = self.right_margin
        self.center_ = self.center

    def restore(self):
        self.left_margin = self.left_margin_
        self.right_margin = self.right_margin_
        self.center = self.center_


class MedianOfTwo():

    def __init__(self, arr1, arr2):
        self.arr1 = Array(arr1)
        self.arr2 = Array(arr2)
        # self.left_margin = self.arr2.left_margin
        # self.right_margin = self.arr2.right_margin
        #TODO: remove simplification
        self.median_position = (len(self.arr1.arr) + len(self.arr2.arr)) // 2

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

    def _find_position(self, arr, point):
        '''
        Finds closet less
        '''
        while (arr.right_margin - arr.left_margin) > 1:
            if arr.center > point:
                self._go_left(arr)
            else:
                self._go_right(arr)
        if arr.right_margin != point:
            return arr.left_margin
        return arr.right_margin

    def _final_logic(self, left_pointer, right_pointer):
        if (left_pointer < self.median_position) & (right_pointer > self.median_position):
            shift = self.median_position - self.arr1.left_margin
            print(f'Median element --> {self.arr2.arr[self.arr2.left_margin+shift]}')
        elif left_pointer > self.median_position:
            print(f'Median element --> {self.arr2.arr[self.median_position]}')
        else:
            print(f'Median element --> {self.arr1.arr[self.median_position]}')

    def get_median(self):
        while (self.arr1.right_margin - self.arr1.left_margin) > 1:
            self.arr2.snapshot()
            arr2_less_equal_el = self._find_position(self.arr2, self.arr1.center)
            self.arr2.restore()
            if self.arr1.center + arr2_less_equal_el > self.median_position:
                self._go_left(self.arr1)
                self._go_right_to_point(self.arr2, arr2_less_equal_el)
            elif self.arr1.center + arr2_less_equal_el < self.median_position:
                self._go_right(self.arr1)
                self._go_left_to_point(self.arr2, arr2_less_equal_el)
            else:
                print(f'Median element --> {self.arr1.center}')
                return
        left_pointer = self.arr1.left_margin + self.arr2.left_margin
        right_pointer = self.arr1.right_margin + self.arr2.right_margin
        self._final_logic(left_pointer, right_pointer)


MedianOfTwo(list(range(10)), list(range(7))).get_median()





