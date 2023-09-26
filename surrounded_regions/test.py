from pytest import mark
from decision import Solution


@mark.parametrize('board, answer', [
    ([["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]],
     [["O","X","X","O","X"],["X","X","X","X","O"],["X","X","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]]),

    ([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]],
    [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]),

    ([["X","X","O","X","X","O","X","O"],["X","X","X","O","X","X","O","X"],["X","X","X","O","X","O","X","O"],["O","X","X","X","X","O","O","X"],["O","O","O","X","O","O","O","X"],["O","X","O","O","X","X","O","X"],["O","X","O","O","X","O","X","X"],["O","X","X","X","O","O","O","X"]],
[["X","X","O","X","X","O","X","O"],["X","X","X","X","X","X","X","X"],["X","X","X","X","X","X","X","O"],["O","X","X","X","X","X","X","X"],["O","O","O","X","X","X","X","X"],["O","X","O","O","X","X","X","X"],["O","X","O","O","X","O","X","X"],["O","X","X","X","O","O","O","X"]]
     )

                                   ]
                  )
def test_jump(board, answer):
    assert Solution().solve(board) == answer