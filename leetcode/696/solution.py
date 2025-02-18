class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans = 0
        for left in range(len(s) - 1):
            right = left + 1
            original_left = s[left]
            original_right = s[right]
            if  original_left == original_right:
                continue

            ans += 1
            while left > 0 and right < len(s) - 1:
                if s[left - 1] == original_left and s[right + 1] == original_right:
                    ans += 1
                    left -= 1
                    right += 1
                else:
                    break
                
        return ans