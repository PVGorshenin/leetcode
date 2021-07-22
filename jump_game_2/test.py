from pytest import mark
from decision import Solution

@mark.parametrize('nums, answer', [([2,3,1,1,4], 2),
                                    ([2,3,0,1,4], 2),
                                   ([1, 2], 1),
                                   ([0], 0),
                                   ([1, 2], 1),
                                   ([3, 2, 4, 2, 6, 7, 8], 2)
                                         ]
                  )
def test_jump(nums, answer):
    assert Solution().jump(nums) == answer