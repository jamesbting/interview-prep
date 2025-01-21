class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        if t == s:
            return s

        #sliding window
        #count chars in t
        t_chars = defaultdict(int)
        for c in t:
            t_chars[c] += 1
        
        window_chars = defaultdict(int)
        required = len(t_chars)
        formed = 0
        left, right = 0, 0
        ans = math.inf, None, None
        while right < len(s):
            c = s[right]
            window_chars[c] += 1
            if c in t_chars and window_chars[c] == t_chars[c]:
                formed += 1
            
            while left <= right and formed == required:
                c = s[left]
                window_chars[c] -= 1
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)
               

                if c in t_chars and window_chars[c] < t_chars[c]:
                    formed -= 1
                left += 1
            right += 1
            
        return "" if ans[0] == math.inf else s[ans[1] : ans[2] + 1]

