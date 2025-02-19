# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        num_list = []
        self.getOrder(root, num_list)

        return self.buildTree(num_list, 0, len(num_list) - 1)
        
    def buildTree(self, lst, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        left_tree = self.buildTree(lst, start, mid - 1)
        right_tree = self.buildTree(lst, mid + 1, end)

        return TreeNode(lst[mid], left_tree, right_tree)
        
        

    def getOrder(self, root, lst):
        if root is None:
            return

        self.getOrder(root.left, lst)
        lst.append(root.val)
        self.getOrder(root.right, lst)        
        
