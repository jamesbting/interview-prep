from collections import deque
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # build a graph
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)
        
        self.reachable = [set() for _ in range(numCourses)]

        #populate the reachables
        for i in range(numCourses):
            self.dfs(i, i, [False for _ in range(numCourses)], graph)

        return [v in self.reachable[u] for u, v in queries]

    def dfs(self, curr, start, visited, graph):
        visited[curr] = True
        self.reachable[start].add(curr)
        for neighbour in graph[curr]:
            if not visited[neighbour]:
                self.dfs(neighbour, start, visited, graph)        