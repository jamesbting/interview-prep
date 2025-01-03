class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:

        graph = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))


        max_prob = [0.0] * n
        max_prob[start_node] = 1
        pq = [(-1.0, start_node)]

        while len(pq) > 0:
            curr_prob, curr_node = heapq.heappop(pq)

            if curr_node == end_node:
                return max_prob[curr_node]

            if graph[curr_node]:
                for neighbour, path_prob in graph[curr_node]:
                    if -curr_prob * path_prob > max_prob[neighbour]:
                        max_prob[neighbour] = -curr_prob * path_prob
                        heapq.heappush(pq, (curr_prob * path_prob, neighbour))

                graph[curr_node] = []

        return 0.0