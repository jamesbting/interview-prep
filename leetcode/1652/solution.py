class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0 for _ in range(len(code))]

        n = len(code)

        decrypted = [0 for _ in range(n)]

        for i in range(n):
            total = 0
            if k > 0:
                j = (i + 1) % n 
                for _ in range(k):
                    total += code[j]
                    j = (j + 1) % n 

            if k < 0:
                j = (i - 1) % n 
                for _ in range(abs(k)):
                    total += code[j]
                    j = (j - 1) % n 

            decrypted[i] = total
        return decrypted
            