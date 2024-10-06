from functools import cmp_to_key

class Solution:

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        last_end = intervals[0][1]
        i, removed = 1, 0
        while i < len(intervals):
            if intervals[i][0] < last_end:
                removed += 1
            else:
                last_end = intervals[i][1]
            i += 1
        return removed