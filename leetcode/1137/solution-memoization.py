class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        
        mem = [-1 for i in range(0, n + 1)]
        mem[0] = 0
        mem[1], mem[2] = 1, 1
        return self.tribonacciWithMem(n, mem)

    def tribonacciWithMem(self, n: int, mem: List[int]):
        if mem[n] != -1:
            return mem[n]
        
        mem[n] = self.tribonacciWithMem(n - 3, mem) + self.tribonacciWithMem(n - 2, mem) + self.tribonacciWithMem(n - 1, mem)
        return mem[n]