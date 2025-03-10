# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p:
            return not q
        if not q:
            return False

        if not p.left and not q.left and not p.right and not q.right:
            return p.val == q.val

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) and p.val == q.val