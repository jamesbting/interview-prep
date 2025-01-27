class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # build a graph
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)
        
        self.numCourses = numCourses
        ans = [
            self.startDfs(u, v,[False for _ in range(numCourses)], graph) for u, v in queries
        ]

        return ans

    def startDfs(self, start, dest, visited, graph):
        for i in range(self.numCourses):
            if not visited[i] and self.dfs(start, dest, visited, graph):
                return True
        return False


        
    def dfs(self, curr, dest, visited, graph):
        if curr == dest:
            return True

        visited[curr] = True
        for neighbour in graph[curr]:
            if not visited[neighbour] and self.dfs(neighbour, dest, visited, graph):
                return True
        return False
        