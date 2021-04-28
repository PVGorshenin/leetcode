from codility import solution
from pytest import mark

@mark.parametrize('input, answer', [([1, 2, 3], 1),
                                    ([1], -2),
                                    ([1, 100000003], -1)
                                    ]
                  )
def test_solution(input, answer):
    assert solution(input) == answer