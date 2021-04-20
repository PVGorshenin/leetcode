from longest_substring_no_repeat import Solution
from pytest import mark

@mark.parametrize('input_str, answer', [('abv', 3),
                                        ('a', 1),
                                        ('abvbv', 3),
                                        ('abcabcbb', 3),
                                        ('bbbbb', 1),
                                        ('', 0)
                                        ]
                  )
def test_solution(input_str, answer):
    assert Solution().lengthOfLongestSubstring(input_str) == answer