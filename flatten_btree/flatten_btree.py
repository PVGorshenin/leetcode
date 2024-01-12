class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        _ = self.dfs(root)

    def dfs(self, root):
        if root is not None:
            last = root
            print('<---', root.val)

            if root.left is not None:
                print('val', root.left.val)
                last = self.dfs(root.left)
                last.right = root.right
                root.right = root.left
                root.left = None

            if last.right is not None:
                last = self.dfs(last.right)

            print(root.val, last.val)

            return last