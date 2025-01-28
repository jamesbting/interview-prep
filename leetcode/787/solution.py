from collections import deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #use bfs to fina all paths <= k + 1 in length and then take the cheapest one\

        #build a graph
        graph = defaultdict(list)
        for frm, to, price in flights:
            graph[frm].append((to, price))


        #do bfs
        dist = [math.inf for _ in range(n)]
        stops = 0
        q = deque([(src, 0)])
        visited = set()
        while q and stops <= k:
            curr_len = len(q)
            for i in range(curr_len):
                curr, distance = q.popleft()
                
                for neighbour, price in graph[curr]:
                    if distance + price >= dist[neighbour]:
                        continue
                    
                    dist[neighbour] = distance + price
                    q.append((neighbour, dist[neighbour]))
            
            stops += 1
            
        return -1 if dist[dst] == math.inf else dist[dst]