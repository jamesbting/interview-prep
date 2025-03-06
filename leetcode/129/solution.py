# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
      self.ans = 0
      self.helper(root, 0)
      return self.ans

    def helper(self, root, curr):
        if root is None:
            return
        
        new_path = (curr * 10) + root.val
        if root.left is None and root.right is None:
            self.ans += new_path

        self.helper(root.left, new_path)
        self.helper(root.right, new_path)