class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj_lst = {}
        for road in roads:
            a,b,d = road
            if a not in adj_lst:
                adj_lst[a] = []
            if b not in adj_lst:
                adj_lst[b] = []
            adj_lst[a].append((b, d))
            adj_lst[b].append((a, d))


        queue = []
        queue.append(1)
        seen = set()
        ans = 10**4 + 1
        while queue:
            curr = queue.pop(0)
            if curr not in seen:
                seen.add(curr)
                for children in adj_lst[curr]:
                    c, d = children
                    queue.append(c)
                    ans = min(ans, d)
        
        return ans