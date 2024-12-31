import heapq

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        l, r = 0 , len(costs) - 1
        leftHeap = []
        rightHeap = []

        cost = 0

        while k > 0:
            while len(leftHeap) < candidates and l <= r:
                heappush(leftHeap, costs[l])
                l += 1
            
            while len(rightHeap) < candidates and l <= r:
                heappush(rightHeap, costs[r])
                r -= 1

            if len(leftHeap) == 0:
                heappush(leftHeap, math.inf)
            if len(rightHeap) == 0:
                heappush(rightHeap, math.inf)
            cost += heappop(leftHeap) if leftHeap[0] <= rightHeap[0] else heappop(rightHeap)
            k -= 1


        return cost