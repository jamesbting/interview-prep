"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        #if node.parent is none then node.right
        #if node.val == parent.left.val then return parent
        #if node.val == parent.right.val then inorder successor(parent)
        root = node
        while root.parent is not None:
            root = root.parent
        traversal = []
        self.dfs(root, traversal)

        for i in range(len(traversal) - 1):
            if traversal[i].val == node.val:
                return traversal[i + 1]
        return None

    def dfs(self, root, traversal):
        if root is None:
            return

        self.dfs(root.left, traversal)
        traversal.append(root)
        self.dfs(root.right, traversal)
            

        