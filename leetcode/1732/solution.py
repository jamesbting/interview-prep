class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_alt = 0
        net_alt = 0
        for x in gain:
            net_alt += x
            max_alt = max(max_alt, net_alt)
        return max_alt