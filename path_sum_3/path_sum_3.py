from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.n_path_w_sum = 0

    def pathSum(self, root: Optional[TreeNode], target_sum: int) -> int:

        self.test_path(root, target_sum)

        if root is not None:
            _ = self.pathSum(root.left, target_sum)
            _ = self.pathSum(root.right, target_sum)

        return self.n_path_w_sum


    def test_path(self, node, curr_sum):

        if node is None:
            return

        if node.val == curr_sum:
            self.n_path_w_sum += 1

        self.test_path(node.left, curr_sum - node.val)
        self.test_path(node.right, curr_sum - node.val)


