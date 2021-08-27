from pytest import mark
from trapping_water import Solution

@mark.parametrize('height, answer', [([3, 0, 1], 1),
                                     ([2, 3, 1], 0),
                                     ([2, 1, 3, 1, 4], 3),
                                     ([4, 2, 0, 3, 2, 5], 9),
                                     ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
                                     ([4, 8, 8, 4], 0),
                                     (list(range(10000)), 0),
                                     (list(range(10000, 0, -1)), 0)]
                  )
def test_trapping(height, answer):
    assert Solution().trap(height) == answer