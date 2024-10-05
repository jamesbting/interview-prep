class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count_map = {}

        for x in arr:
            if x not in count_map:
                count_map[x] = 1
            else:
                count_map[x] += 1

        return len(set(count_map.values())) == len(count_map)