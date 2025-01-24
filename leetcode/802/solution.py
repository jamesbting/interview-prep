from collections import deque
class Solution:
    def dfs(self, node, graph, visited, inStack):
        if inStack[node]: # we have a cycle
            return True
        if visited[node]:
            return False

        visited[node] = True
        inStack[node] = True
        for neighbour in graph[node]:
            if self.dfs(neighbour, graph, visited, inStack):
                return True
        inStack[node] = False
        return False

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)

        visited = [False for _ in range(n)]
        inStack = [False for _ in range(n)]

        for i in range(n):
            self.dfs(i, graph, visited, inStack)

        ans = []
        for i in range(n):
            if not inStack[i]:
                ans.append(i)
        return ans
