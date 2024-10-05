# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        print(self.getLeafSequence(root1)) 
        print(self.getLeafSequence(root2))
        return self.getLeafSequence(root1) == self.getLeafSequence(root2)

    def getLeafSequence(self, tree) -> List[int]:
        stack = [tree]
        sequence = []

        while len(stack) > 0:
            curr = stack.pop()
            if curr.left is None and curr.right is None:
                sequence.append(curr.val)

            if curr.left is not None:
                stack.append(curr.left)
            if curr.right is not None:
                stack.append(curr.right)
                
        return sequence