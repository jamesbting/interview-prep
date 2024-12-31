"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        self.connectRecursive(root, None)
        return root
        
    
    def connectRecursive(self, root, right_node):
        if root is None:
            return
        root.next = right_node
        if root.left is not None:
            self.connectRecursive(root.left, root.right)
            self.connectRecursive(root.right, root.next.left if root.next is not None else None)
