class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        self.ans = -1
        visited = [False for _ in range(len(edges))]
        for i in range(len(edges)):
                dist = {i: 1}
                self.dfs(i, visited, dist, edges)

        return self.ans


    def dfs(self, node, visited, dist, edges):
        visited[node] = True
        if edges[node] != -1 and not visited[edges[node]]:
            dist[edges[node]] = dist[node] + 1
            self.dfs(edges[node], visited, dist, edges)
        elif edges[node] != -1 and edges[node] in dist:
            self.ans = max(self.ans, dist[node] - dist[edges[node]] + 1)