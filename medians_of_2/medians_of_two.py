import numpy as np

class Array():
    def __init__(self, arr):
        self.arr = arr
        self.left_margin = 0
        self.right_margin = len(arr)-1
        self.center = (len(arr) - 1)// 2

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
        self.is_odd = (len(arr1) + len(arr2)) % 2
        self.median_position = (len(self.arr1.arr) + len(self.arr2.arr) - 1) // 2

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

    def _find_position(self, arr2, point):
        '''
        Finds closet less
        '''
        while (arr2.right_margin - arr2.left_margin) > 1:
            if arr2.arr[arr2.center] > point:
                self._go_left(arr2)
            else:
                self._go_right(arr2)
        if arr2.arr[arr2.right_margin] <= point:
            return arr2.right_margin
        return arr2.left_margin

    def _odd_logic(self, left_pointer, right_pointer):
        if (left_pointer < self.median_position) & (right_pointer > self.median_position):
            shift = self.median_position - left_pointer
            return self.arr2.arr[self.arr2.left_margin + shift]
        elif left_pointer > self.median_position:
            return self.arr2.arr[self.median_position]
        elif right_pointer < self.median_position:
            return self.arr2.arr[self.median_position - len(self.arr1.arr)]

    def _final_logic(self, left_pointer, right_pointer):
        if self.is_odd:
            return self._odd_logic(left_pointer, right_pointer)
        else:
            left_el = self._odd_logic(left_pointer, right_pointer)
            next_el_shift = 1
            self.median_position += next_el_shift
            if right_pointer == self.median_position:
                right_el = self.arr1.arr[self.arr1.right_margin]
            else:
                right_el = self._odd_logic(left_pointer, right_pointer)
            return (left_el + right_el) / 2

    def _find_zero_numeration_shift(self):
        #todo: обобщить на случай, когда 0 не входит
        return 1

    def _check_center_pos(self):
        return self.arr1.arr[self.arr1.center]

    def _unintersect_script(self, arr1, arr2):
        if arr1.arr[-1] < arr2.arr[0]:
            if arr1.right_margin >= self.median_position:
                left_el = arr1.arr[self.median_position]
                if not self.is_odd:
                    if arr1.right_margin >= (self.median_position+1):
                        right_el = arr1.arr[self.median_position+1]
                    else:
                        right_el = arr2.arr[0]
                    print(f'Median element uninter1--> {.5 * (left_el + right_el)}')
                    return True
                print(f'Median element uninter1--> {left_el}')
                return left_el
            else:
                shift = self.median_position - arr1.right_margin - 1
                left_el = arr2.arr[shift]
                if not self.is_odd:
                    right_el = arr2.arr[shift+1]
                    print(f'Median element uninter1--> {.5 * (left_el + right_el)}')
                    return True
                print(f'Median element uninter--> {left_el}')
                return True

    def get_median(self):
        if self._unintersect_script(self.arr1, self.arr2): return
        if self._unintersect_script(self.arr2, self.arr1): return
        while (self.arr1.right_margin - self.arr1.left_margin) > 1:
            self.arr2.snapshot()
            arr2_less_equal_el = self._find_position(self.arr2, self.arr1.arr[self.arr1.center])
            self.arr2.restore()
            zero_numeration_shift = self._find_zero_numeration_shift()
            if self.arr1.center + arr2_less_equal_el + zero_numeration_shift > self.median_position:
                self._go_left(self.arr1)
                self._go_left_to_point(self.arr2, arr2_less_equal_el)
            elif self.arr1.center + arr2_less_equal_el + zero_numeration_shift < self.median_position:
                self._go_right(self.arr1)
                self._go_right_to_point(self.arr2, arr2_less_equal_el)
            elif self.is_odd:
                median = self._check_center_pos()
                print(f'Median element dosr1--> {median}')
                return
            else:
                left_el = self._check_center_pos()
                next_el_shift = 1
                right_el = min(self.arr1.arr[self.arr1.center+next_el_shift],
                               self.arr2.arr[arr2_less_equal_el+next_el_shift])
                print(f'Median element dosr2--> { (left_el + right_el) / 2}')
                return
        zero_numeration_shift = self._find_zero_numeration_shift()
        left_pointer = self.arr1.left_margin + self.arr2.left_margin + zero_numeration_shift

        zero_numeration_shift = self._find_zero_numeration_shift()
        right_pointer = self.arr1.right_margin + self.arr2.right_margin + zero_numeration_shift
        median_el = self._final_logic(left_pointer, right_pointer)
        print(f'Median element --> {median_el}')

a = list(range(17, 23))
b = list(range(23, 45))
MedianOfTwo(a, b).get_median()

def find_median(a, b):
    print()
    print('np median -->', np.median(a+b))
    print(sorted(a+b))

find_median(a, b)





