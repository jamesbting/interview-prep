class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count_map = defaultdict(int)

        for word in words:
            count_map[word] += 1

        heap = []

        for word, count in count_map.items():
            heapq.heappush(heap, (-count, word))
        
        return [heapq.heappop(heap)[1] for _ in range(k)]