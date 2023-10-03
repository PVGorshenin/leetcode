from typing import List

def binary_search(arr, value, left=0, right=None, is_x=True):

    if right is None:
        right = len(arr) - 1

    idx_in_tuple = 1
    if is_x:
        idx_in_tuple = 0

    while right - left > 1 :
        mid = left + (right - left) // 2
        if arr[mid][idx_in_tuple] == value:
            return mid
        elif arr[mid][idx_in_tuple] < value:
            left = mid
        else:
            right = mid

    if value >= arr[right][idx_in_tuple]:
            left = right

    if value <= arr[left][idx_in_tuple]:
            right = left

    if idx_in_tuple:
        return right

    return left


class Solution:

    def _two_elements(self, left_interval, right_interval):

        merged_intervals = []

        x1, y1 = left_interval
        x2, y2 = right_interval

        in_middle_of_first_interval = x1 <= x2 <= y1
        in_middle_of_second_interval = x2 <= x1 <= y2

        if in_middle_of_first_interval:
            x_current = x1
            y_current = max(y1, y2)
            merged_intervals.append([x_current, y_current])

        elif in_middle_of_second_interval:
            x_current = x2
            y_current = max(y1, y2)
            merged_intervals.append([x_current, y_current])

        elif y1 < x2:
            merged_intervals.extend([left_interval, right_interval])

        elif y2 < x1:
            merged_intervals.extend([right_interval, left_interval])

        return merged_intervals

    def _final_merge(self, merged_intervals, interval_pos_of_x, interval_pos_of_y, is_middle_or_outer_of_left,
                     is_middle_or_outer_of_right, is_in_both_intervals):

        if interval_pos_of_x - is_middle_or_outer_of_left == -1:
            left_part = []
        else:
            left_part = merged_intervals[:interval_pos_of_x + 1 - is_middle_or_outer_of_left]

        if is_in_both_intervals and interval_pos_of_y == len(merged_intervals):
            right_part = []
        elif interval_pos_of_y + is_middle_or_outer_of_right == len(merged_intervals):
            right_part = []
        else:
            is_middle_or_outer_or_inleft = is_middle_or_outer_of_right | is_in_both_intervals
            right_part = merged_intervals[interval_pos_of_y + is_middle_or_outer_or_inleft:]

        return left_part, right_part

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        len_intervals = len(intervals)

        if len(intervals) <= 1:
            return intervals

        merged_intervals = self._two_elements(
            left_interval=intervals[0],
            right_interval=intervals[1]
        )
        intervals = intervals[2:]

        if len_intervals == 2:
            return merged_intervals

        for interval in intervals:
            x, y = interval

            if len(merged_intervals) < 2:
                merged_intervals = self._two_elements(
                    left_interval=merged_intervals[0],
                    right_interval=interval
                )
                continue

            interval_pos_of_x = binary_search(
                arr=merged_intervals,
                value=x,
                left=0,
                is_x=True
            )

            x_left_interval, y_left_interval = merged_intervals[interval_pos_of_x]

            interval_pos_of_y = binary_search(
                arr=merged_intervals,
                value=y,
                left=max(0, interval_pos_of_x-1),
                is_x=False
            )

            interval_pos_of_y = max(interval_pos_of_x, interval_pos_of_y)

            is_in_both_intervals = interval_pos_of_x == interval_pos_of_y

            x_right_interval, y_right_interval = merged_intervals[interval_pos_of_y]

            is_left_intersected = (x <= y_left_interval) and (y >= x_left_interval)
            is_right_intersected = (x <= y_right_interval) and (y >= x_right_interval)

            x_min = x
            y_max = y

            if is_left_intersected:
                x_min = min(x, x_left_interval)
                y_max = max(y, y_left_interval)

            if is_right_intersected:
                y_max = max(y_max, y_right_interval)

            left_part, right_part = self._final_merge(
                merged_intervals,
                interval_pos_of_x,
                interval_pos_of_y,
                is_left_intersected,
                is_right_intersected,
                is_in_both_intervals
            )

            is_margin_left = (interval_pos_of_x == 0) and (not is_left_intersected) and (x < x_left_interval)
            is_margin_right = ((interval_pos_of_x == len(merged_intervals)-1) and (not is_right_intersected)
                               and (y > y_right_interval))

            if is_margin_left:
                merged_intervals = [[x_min, y_max]] + left_part + right_part
            elif is_margin_right:
                merged_intervals = left_part + right_part + [[x_min, y_max]]
            else:
                merged_intervals = (left_part + [[x_min, y_max]] + right_part)

        return merged_intervals




