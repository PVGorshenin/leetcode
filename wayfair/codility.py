import numpy as np


def solution(A):
    assert isinstance(A, list)
    assert (len(A) > 0) & (len(A) <= 40000)
    assert (min(A) > -2147483649) & (max(A) < 2147483649)
    if len(A) == 1:
        return -2
    a_np = np.array(A)
    a_np.sort()
    a_shifted = a_np[1:]
    dist_arr = a_np[:-1] - a_shifted
    res = np.min(np.abs(dist_arr))
    max_alowed_dist = 100000000
    if res > max_alowed_dist:
        return -1
    return res


