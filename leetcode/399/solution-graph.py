class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        nodes = set()
        for i in range(len(equations)):
            u, v = equations[i]
            graph[u][v] = values[i]
            graph[v][u] = 1 / values[i]
            nodes.add(u)
            nodes.add(v)

        return [self.dfs(graph, u, v, set()) if u in nodes and v in nodes else -1.0 for u, v in queries]


    def dfs(self, graph, u, v, visited):
        if u == v:
            return 1.0

        for n in graph[u]:
            if n in visited:
                continue
            visited.add(n)
            cost = self.dfs(graph, n, v, visited)
            if cost != -1.0:
                return cost * graph[u][n]

        return -1.0