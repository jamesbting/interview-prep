class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        max_on_right = 0
        ans = []
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > max_on_right:
                ans.append(i)
                max_on_right = heights[i]
        return ans[::-1]