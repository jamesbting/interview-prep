# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_path = self.findPathDFS(root, p)
        q_path = self.findPathDFS(root, q)
        
        i = 0
        while i < len(p_path) and i < len(q_path):
            if p_path[i] != q_path[i]:
                break
            i += 1

        return p_path[i - 1]
    
    def findPathDFS(self, root: 'TreeNode', p: 'TreeNode') -> List['TreeNode']:
        if root == None:
            return None

        if p == root:
            return [root]

        left = self.findPathDFS(root.left, p)
        if left:
            left.insert(0, root)
            return left
            
        right = self.findPathDFS(root.right, p)
        if right:
            right.insert(0, root)
            return right

        return None
