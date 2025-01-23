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
        #node is in upper part of the tree
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node

        #node is not the root, and next node to travers is above it
        while node.parent and node == node.parent.right:
            node = node.parent
        return node.parent
            

        