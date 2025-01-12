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

        currLevel = []
        nextLevel = []
        views = []
        level = 0
        currLevel.append(root)
        while len(currLevel) > 0:
            curr = currLevel.pop(0)
            if level >= len(views):
                views.append(curr.val)
            else:
                views[level] = curr.val

            if curr.left is not None:
                nextLevel.append(curr.left)
            if curr.right is not None:
                nextLevel.append(curr.right)

            if len(currLevel) == 0:
                currLevel = nextLevel
                nextLevel = []
                level += 1
        return views


