class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.mem = {}

        def dfs(rem):
            if rem < 0:
                return -1

            if rem == 0:
                return 0
            
            if rem in self.mem:
                return self.mem[rem]
            ans = math.inf
            for coin in coins:
                res = dfs(rem - coin)
                if res != -1:
                    ans = min(ans, res + 1)
            
            self.mem[rem] = -1 if ans == math.inf else ans 
            return -1 if ans == math.inf else ans 
        
        return dfs(amount)

 