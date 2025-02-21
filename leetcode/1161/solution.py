# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        level = 1
        max_sum = -math.inf
        sum_levels = {}
        while q:
            l = len(q)
            curr_sum = 0
            for i in range(l):
                curr = q.popleft()
                curr_sum += curr.val
                if curr.left is not None:
                    q.append(curr.left)
                if curr.right is not None:
                    q.append(curr.right)

            
            max_sum = max(max_sum, curr_sum)
            if max_sum not in sum_levels:
            level += 1
                sum_levels[max_sum] = level

        return sum_levels[max_sum]
                