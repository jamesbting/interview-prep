# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q = deque([root, None])
        level_list = deque()
        ans = []
        order_left = True
        while q:
            curr = q.popleft()
            if curr is None:
                ans.append(list(level_list))
                if len(q) > 0:
                    q.append(None)
                level_list = deque()
                order_left = not order_left
            else:
                if order_left:
                    level_list.append(curr.val)
                else:
                    level_list.appendleft(curr.val)
                if curr.left is not None: q.append(curr.left)
                if curr.right is not None: q.append(curr.right)
        return ans

        