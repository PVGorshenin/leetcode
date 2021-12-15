from pytest import mark
from decision import check_ax_of_refl


@mark.parametrize('src_arr, answer', [([(2, 1), (4, 1)], True),
                                     ([(2, 1), (4, 1), (3, 1)], True),
                                      ([(10, 20), (11, 22)], False),
                                      ([(1, 3), (5, 3), (3, 3), (0, 2), (6, 2)], True)
                                      ]
                  )
def test_reflection(src_arr, answer):
    assert check_ax_of_refl(src_arr) == answer
