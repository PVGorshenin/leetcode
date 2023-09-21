from pytest import mark
from medians_of_two import Solution


@mark.parametrize('nums1, nums2, answer', [
    ([0, 0], [0, 0], 0),
    ([], [0], 0),
    ([1, 3], [2, 7], 2.5),
    ([1, 3], [2], 2),
    ([3], [-2, -1], -1),
    ([1, 3, 4, 5, 6], [1], 3.5),
    ([1, 3], [2, 4, 5, 6], 3.5),
    ([1, 2, 4], [3, 5, 6], 3.5),
    ([1, 4, 5], [2, 3, 6], 3.5),
    ([3, 4, 5], [1, 2, 6], 3.5),
    ([1, 2, 4], [3, 5, 6, 7], 4)
                                   ]
                  )
def test_jump(nums1, nums2, answer):
    assert Solution().findMedianSortedArrays(nums1, nums2) == answer