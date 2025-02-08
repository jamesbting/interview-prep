class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        window_chars = set()
        left = 0
        for right in range(len(s)):
            while s[right] in window_chars:
                window_chars.remove(s[left])
                left += 1
            window_chars.add(s[right])
            ans = max(ans, right - left + 1)
        return ans
            