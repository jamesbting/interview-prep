# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        lst = deque()
        lst.append(p)
        lst.append(q)

        while lst:
            n1, n2 = lst.popleft(), lst.popleft()
            if not n1 and not n2:
                continue
            if (n1 and not n2) or (n2 and not n1) or n1.val != n2.val:
                return False
            lst.append(n1.left)
            lst.append(n2.left)
            lst.append(n1.right)
            lst.append(n2.right)
        return True