class Solution:
    def countPalindromes(self, s: str) -> int:
        mod, n, ans = 10**9 + 7, len(s), 0

        prefixes, counts = [[[0 for _ in range(1)] * 10 for _ in range(10)] for _ in range(n)], [0] * 10
        for i in range(n):
            c = int(s[i])
            if i:
                for j in range(10):
                    for k in range(10):
                        prefixes[i][j][k] = prefixes[i - 1][j][k]
                        if k == c:
                            prefixes[i][j][k] += counts[j]
            counts[c] += 1
        
        suffixes, counts = [[[0 for _ in range(10)] for _ in range(10)] for _ in range(n)], [0] * 10
        for i in range(n -1 , -1 , -1):
            c = int(s[i])
            if i < n - 1:
                for j in range(10):
                    for k in range(10):
                        suffixes[i][j][k] = suffixes[i + 1][j][k]
                        if k == c:
                            suffixes[i][j][k] += counts[j]
            counts[c] += 1
        
        for i in range(2, n - 2):
            for j in range(10):
                for k in range(10):
                    ans += prefixes[i - 1][j][k] * suffixes[i + 1][j][k]
        return ans % mod