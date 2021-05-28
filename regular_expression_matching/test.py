from regular_expression_matching import Solution
from pytest import mark

@mark.parametrize('input_str, pattern, answer', [('aa', 'a', False),
                                                ('a', 'a', True),
                                                ('aa', 'a*', True),
                                                 ('aa', 'aaa*', True),
                                                 ('aab', 'a*', False),
                                                ('aab', 'a*b', True),
                                                ('b', 'a*b', True),
                                                ]
                  )
def test_letter_symbol(input_str, pattern, answer):
    assert Solution().isMatch(input_str, pattern) == answer


@mark.parametrize('input_str, pattern, answer', [('ad', 'a.', True),
                                                ('a', 'a.', False),
                                                ('ad', 'a.*', True),
                                                ('assdfsdfsdf', 'a.*', True),
                                                ('assdsdsdf', 'a.*f', True),
                                                ('assususdf', 'a.*df', True)
                                                 ]
                  )
def test_any_symbol(input_str, pattern, answer):
    assert Solution().isMatch(input_str, pattern) == answer


@mark.parametrize('input_str, pattern, answer', [('aa', 'a*', True),
                                                 ('ab', '.*', True),
                                                 ('aab', 'c*a*b', True),
                                                 ('mississippi', 'mis*is*p*.', False),
                                                 ('aaa', 'a*a', True),
                                                 ('aaa', 'a.*a', True),
                                                 ('aaa', 'ab*a*c*a', True),
                                                 ('aaa', 'aa*b*ac*', True),
                                                 ('aaa', 'aa*.*ac*', True),
                                                 ]
                  )
def test_site_ex(input_str, pattern, answer):
    assert Solution().isMatch(input_str, pattern) == answer