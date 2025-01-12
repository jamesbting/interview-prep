# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rightMost = []
        self.rightSideViewRec(root, 0, rightMost)
        return rightMost


    def rightSideViewRec(self, root: Optional[TreeNode], currLevel: int, rightMost: List[int]) -> None:
        if root is None:
            return
        if root.left is None and root.right is None:
            if currLevel >= len(rightMost):
                rightMost.append(root.val)
            else:
                rightMost[currLevel] = root.val
            return

        if currLevel >= len(rightMost):
            rightMost.append(root.val)
        else:
            rightMost[currLevel] = root.val
            
        self.rightSideViewRec(root.left, currLevel + 1, rightMost)
        self.rightSideViewRec(root.right, currLevel + 1, rightMost)

