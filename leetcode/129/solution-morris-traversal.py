# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans, curr_number = 0, 0
        while root:
            if root.left:
                predecessor = root.left
                steps = 1
                while predecessor.right and predecessor.right is not root:
                    predecessor = predecessor.right
                    steps += 1

                if predecessor.right is None:
                    curr_number = curr_number * 10 + root.val
                    predecessor.right = root
                    root = root.left
                else:
                    if predecessor.left is None:
                        ans += curr_number
                    curr_number //= (10 ** steps)
                    predecessor.right = None
                    root = root.right
            else:
                curr_number = curr_number * 10 + root.val
                if root.right is None:
                    ans += curr_number
                root = root.right
        return ans
