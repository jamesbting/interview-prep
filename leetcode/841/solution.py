class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False for _ in rooms]
        queue = []
        queue.append(0)

        while queue:
            curr = queue.pop(0)
            visited[curr] = True
            keys = rooms[curr]
            for key in keys:
                if not visited[key]:
                    queue.append(key)
            
        for visit in visited:
            if not visit:
                return False

        return True

        