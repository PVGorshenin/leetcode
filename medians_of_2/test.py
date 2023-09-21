from pytest import mark
from medians_of_two import Solution


@mark.parametrize('nums1, nums2, answer', [
    ([0, 0], [0, 0], 0),
    ([], [0], 0),
    ([1, 3], [2, 7], 2.5)
                                   ]
                  )
def test_jump(nums1, nums2, answer):
    assert Solution().findMedianSortedArrays(nums1, nums2) == answer