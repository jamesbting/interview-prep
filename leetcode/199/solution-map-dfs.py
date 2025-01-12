# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        views = {}
        self.dfs(root, views, 0)

        ans = []
        for i in views.keys():
            ans.append(views[i])
        return ans

    def dfs(self, root, views, level):
        if root is None:
            return

        views[level] = root.val
        self.dfs(root.left, views, level + 1)
        self.dfs(root.right, views, level + 1)