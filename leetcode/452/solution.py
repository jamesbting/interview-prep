class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        arrowShots = 0
        lastEnd = -math.inf
        for point in points:
            if point[0] > lastEnd:
                arrowShots += 1
                lastEnd = point[1]

        return arrowShots
