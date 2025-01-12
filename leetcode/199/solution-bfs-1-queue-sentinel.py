# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []

        q = []
        views = []
        level = 0
        q.append(root)
        q.append(None)
        curr = root
        while len(q) > 0:
            prev, curr = curr, q.pop(0)
            while curr:
                if curr.left is not None:
                    q.append(curr.left)
                if curr.right is not None:
                    q.append(curr.right) 
                prev, curr = curr, q.pop(0)
           
            views.append(prev.val)
            if len(q) > 0:
                q.append(None)
           
        return views


