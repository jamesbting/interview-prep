# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        self.mp = defaultdict(list)
        self.dfs(root, 0, 0)
            
        ans = []
        for i in range(min(self.mp.keys()), max(self.mp.keys()) + 1):
            self.mp[i].sort(key=lambda x:x[0])
            ans.append([val for row, val in self.mp[i]])
        return ans

    def dfs(self, curr, col, row):
        if not curr:
            return
        self.mp[col].append((row, curr.val))
        self.dfs(curr.left, col - 1, row + 1)
        self.dfs(curr.right, col + 1, row + 1)
        