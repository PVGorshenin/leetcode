from regular_expression_matching import Solution
from pytest import mark

@mark.parametrize('input_str, pattern, answer', [('aa', 'a', False),
                                                ('a', 'a', True),
                                                ('aa', 'a*', True),
                                                ('aab', 'a*', False),
                                                ('aab', 'a*b', True),
                                                ]
                  )
def test_solution(input_str, pattern, answer):
    assert Solution().isMatch(input_str, pattern) == answer