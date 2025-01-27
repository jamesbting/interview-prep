"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        root = Node(node.val)
        cloned_nodes = {node.val: root}
        cloned_neighbours = defaultdict(list)
        q = deque([node])
        visited = set()

        #clone all the nodes
        while q:
            curr = q.popleft()
            if curr in visited:
                continue
            #create nodes
            cloned_nodes[curr.val] = Node(curr.val)
            visited.add(curr)

            for neighbour in curr.neighbors:
                    q.append(neighbour)
                    cloned_neighbours[curr.val].append(neighbour.val)

        #re build edges
        for clone in cloned_neighbours.keys():
            cloned_nodes[clone].neighbors = [cloned_nodes[neighbour] for neighbour in cloned_neighbours[clone]]

        return cloned_nodes[node.val]