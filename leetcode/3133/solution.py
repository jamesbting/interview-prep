class Solution:
    def minEnd(self, n: int, x: int) -> int:
        out = 0
        n -= 1

        bits_x = [0 for _ in range(64)]
        bits_n = [0 for _ in range(64)]
        

        for i in range(64):
            bit = (x >> i) & 1
            bits_x[i] = bit

            bit = (n >> i) & 1
            bits_n[i] = bit

        posX = 0
        posN = 0
        while posX < 63:
            while posX < 63 and bits_x[posX] != 0:
                posX += 1

            bits_x[posX] = bits_n[posN]
            posX += 1
            posN += 1

        for bit in bits_x[::-1]:
            out = (out << 1) | bit
        return out
