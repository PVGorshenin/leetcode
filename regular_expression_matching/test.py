from regexp_matrices import Solution
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
                                                 ('ab', '.*c', False)
                                                 ]
                  )
def test_site_ex(input_str, pattern, answer):
    assert Solution().isMatch(input_str, pattern) == answer


@mark.parametrize('input_str, pattern, answer', [('a', '.*..a*', False),
                                                ('ab', '.*..', True),
                                                 ('abcdede', 'ab.*de', True),
                                                 ('aaaaaaaaaaaaab', 'a*a*a*a*a*a*a*a*a*a*a*a*b', True),
                                                 ('bbba', '.*b', False),
                                                 ('mississippi', 'mis*is*ip*.', True),
                                                 ('aaba', 'ab*a*c*a', False),
                                                 ('abbbcd', 'ab*bbbcd', True),
                                                 ('aabcbcbcaccbcaabc', ".*a*aa*.*b*.c*.*a*", True),
                                                 ('abbabaaaaaaacaa', "a*.*b.a.*c*b*a*c*", True),
                                                 ('cabbbbcbcacbabc', '.*b.*.ab*.*b*a*c', True),
                                                 ('baabbbaccbccacacc', "c*..b*a*a.*a..*c", True),
                                                 ('bbcacbabbcbaaccabc', "b*a*a*.c*bb*b*.*.*", True),
                                                 ('bccbbabcaccacbcacaa', ".*b.*c*.*.*.c*a*.c", False),
                                                 ('aacaaacbacccbcba', 'c*a*.*a*.a.ac*bc', False),
                                                 ('abbbaabccbaabacab', 'ab*b*b*bc*ac*.*bb*', True),
                                                 ('babbcabcaabbbacaca', 'bb*.c*.c*b*b.*c', False),
                                                 ('aaaaaaaaaaaaaaaaaa', 'a*aaaa*aa.aaa.aaaa.a', True)]
                  )
def test_site_ex2(input_str, pattern, answer):
    assert Solution().isMatch(input_str, pattern) == answer