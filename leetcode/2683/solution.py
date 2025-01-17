    def doesValidArrayExist(self, derived: List[int]) -> bool:
        ans = 0
        for n in derived:
            ans ^= n
        return ans == 0