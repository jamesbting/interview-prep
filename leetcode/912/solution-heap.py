class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heap = []
        for n in nums:
            heapq.heappush(heap, n)

        l = []
        while heap:
            l.append(heapq.heappop(heap))

        return l
   