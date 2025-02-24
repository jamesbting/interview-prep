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

        q = deque()
        mp = defaultdict(list)
        q.append((root, 0))

        while q:
            curr, col = q.popleft()
            if curr is not None:
                mp[col].append(curr.val)
                q.append((curr.left, col - 1))
                q.append((curr.right, col + 1))
            
        return [mp.get(i, []) for i in range(min(mp.keys()), max(mp.keys()) + 1)]