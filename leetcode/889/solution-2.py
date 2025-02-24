# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder:
            return None
        val = postorder.pop()
        root = TreeNode(val)
        if not postorder:
            return root

        i = postorder.index(preorder[1])
        root.left = self.constructFromPrePost(preorder[1:i+2], postorder[:i+1])
        root.right = self.constructFromPrePost(preorder[i+2:], postorder[i+1:])
        return root