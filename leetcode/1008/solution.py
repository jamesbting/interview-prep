# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        self.i = 0
        return self.construct(preorder, - math.inf, math.inf)
      
    def construct(self, preorder, lo, hi):
        i = self.i
        if i == len(preorder) or not (lo < preorder[i] < hi):
            return None
        root = TreeNode(preorder[i])
        self.i += 1
        root.left = self.construct(preorder, lo, preorder[i])
        root.right = self.construct(preorder, preorder[i], hi)
        return root