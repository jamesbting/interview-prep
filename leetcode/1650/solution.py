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
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_path = []
        curr = p
        while curr is not None:
            p_path.append(curr)
            curr = curr.parent

        q_path = []
        curr = q
        while curr is not None:
            q_path.append(curr)
            curr = curr.parent

        i, j = len(p_path) - 1, len(q_path) - 1
        lca = None
        while i > 0 or j > 0:
            if p_path[i] == q_path[j]:
                lca = p_path[i]
            
            i -= 1 if i > 0 else 0
            j -= 1 if j > 0 else 0
        return lca
