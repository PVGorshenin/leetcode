# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:

        depth = 0

        if root is not None:
            depth += 1
            left_hight = self.maxDepth(root.left)
            right_hight = self.maxDepth(root.right)

            depth += max(left_hight, right_hight)

        return depth