class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False


        neighbours = defaultdict(list)
        for u, v in edges:
            neighbours[u].append(v)
            neighbours[v].append(u)


        stack = []
        stack.append(0)
        seen = set()
        seen.add(0)
        while len(stack) > 0:
            curr = stack.pop(0)
            for neighbour in neighbours[curr]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    stack.append(neighbour)

        return len(seen) == n
