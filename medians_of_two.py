import numpy as np

class Array():
    def __init__(self, arr):
        self.arr = arr
        self.left_margin = 0
        self.right_margin = len(arr)
        self.in_left = False


class MedianOfTwo():

    def __init__(self, arr1, arr2):
        self.arr1 = Array(arr1)
        self.arr2 = Array(arr2)
        self.arr1.center = self._get_center(arr1.arr)
        self.arr2.center = self._get_center(arr2.arr)
        self.left_margin = np.NaN
        self.right_margin = np.NaN

    def _get_center(self, arr):
        return np.ceil(len(arr) / 2)

    def _go_left(self, arr):
        self.right_margin = arr.center
        arr.right_margin = arr.center
        arr.center = self._get_center(arr)

    def _go_right(self, arr):
        self.right_margin = arr.center
        arr.left_margin = arr.center
        arr.center = self._get_center(arr)

    def _init_compare(self):
        if self.arr2.center > self.arr1.center:
            self._go_left(self.arr2)
            arr.is_left = True
        else:
            self._go_right(self.arr2)
            arr.is_left = False

    def get_median(self):
        while (self.right_margin - self.left_margin) > 1:




