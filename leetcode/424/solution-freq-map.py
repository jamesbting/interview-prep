max_lenclass Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_arr = [0 for _ in range(26)]
        max_frequency = 0
        max_len = 0
        start = 0
        for end in range(len(s)):
            count_arr[ord(s[end]) - ord('A')] += 1
            max_frequency = max(max_frequency, count_arr[ord(s[end]) - ord('A')])

            if not (end + 1 - start - max_frequency <= k):
               
                count_arr[ord(s[start]) - ord('A')] -= 1
                start += 1
            
            max_len = end + 1 - start
        return max_len

        