# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.pre_i = 0
        self.post_i = 0

        return self.divide(preorder, postorder)

    def divide(self, preorder, postorder):
        root = TreeNode(preorder[self.pre_i])
        self.pre_i += 1

        if root.val != postorder[self.post_i]:
            root.left = self.divide(preorder, postorder)

        if root.val != postorder[self.post_i]:
            root.right = self.divide(preorder, postorder)

        self.post_i += 1
        return root
