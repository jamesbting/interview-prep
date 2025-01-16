
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        heap = []
        total_days = max(end for start, end in events)
        i = 0
        attended = 0
        for day in range(1, total_days + 1):
            #add all the events that start today

            while i < len(events) and events[i][0] == day:
                heapq.heappush(heap, events[i][1])
                i += 1

            while heap and heap[0] < day:
                heapq.heappop(heap)

            if heap:
                attended += 1
                heapq.heappop(heap)

        return attended
        