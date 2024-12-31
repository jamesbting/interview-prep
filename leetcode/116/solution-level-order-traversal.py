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
        #level order traversal
        if root == None:
            return root
        queue = []
        queue.append([root])

        while len(queue) > 0:
            level_nodes = queue.pop(0)

            next_level = []
            for i in range(0, len(level_nodes)):
                node = level_nodes[i]
                node.next = level_nodes[i + 1] if i < len(level_nodes) - 1 else None

                if node.left is not None:
                    next_level.append(node.left)
                    next_level.append(node.right)
            if len(next_level) > 0:
                queue.append(next_level)
        return root