from pytest import mark
from decision import Solution

@mark.parametrize('nums, target, answer', [([4,5,6,7,0,1,2], 0, 4),
                                          ([4,5,6,7,0,1,2], 3, -1),
                                          ([1], 0, -1),
                                           ([], 5, -1),
                                           ([1], 1, 0),
                                           ([1, 2, 3, 4, 5], 5, 4),
                                           ([1, 3], 1, 0),
                                           ([1, 3, 5], 1, 0)]
                  )
def test_search(nums, target, answer):
    assert Solution().search(nums, target) == answer