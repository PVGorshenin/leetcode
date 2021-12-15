from collections import defaultdict
from typing import List


def check_ax_of_refl(src_arr: List[tuple]) -> bool:
    double_median = min(src_arr)[0] + max(src_arr)[0]
    src_arr = [(i_tuple[0] * 2, i_tuple[1]) for i_tuple in src_arr]
    diff_x_arr = [i_tuple[0] - double_median for i_tuple in src_arr]

    y_based_dct = defaultdict(lambda: defaultdict(int))
    for i_point, point in enumerate(src_arr):
        x_shift = diff_x_arr[i_point]
        if x_shift:
            plus_or_minus = int(x_shift / abs(x_shift))
            y_based_dct[point[1]][abs(x_shift)] += plus_or_minus

    for y_point in y_based_dct.values():
        for i_diff_count in y_point.values():
            if i_diff_count:
                return False

    return True





