"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        self.first = None
        self.last = None

        self.toDoublyListHelper(root)

        self.last.right = self.first
        self.first.left = self.last
        return self.first

        
    def toDoublyListHelper(self, node):
        if node is not None:
            self.toDoublyListHelper(node.left)    

            if self.last is not None:
                self.last.right = node
                node.left = self.last
            else:
                self.first = node
            self.last = node

            self.toDoublyListHelper(node.right)
        