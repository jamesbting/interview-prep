class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        all_chars = set(s)
        max_len = 0
        for c in all_chars:
            start = 0
            count = 0

            for end in range(len(s)):
                
                if s[end] == c:
                    count += 1
                
                while not (end + 1 - start - count <= k):
                    if s[start] == c:
                        count -= 1
                    start += 1

                max_len = max(max_len, end + 1 - start)
        return max_len

        
            
