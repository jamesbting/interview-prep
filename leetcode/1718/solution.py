class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        res = [0 for _ in range(n * 2 - 1)]
        used_nums = [False for _ in range(n + 1)]

        self.generate(0, res, used_nums, n)
        return res

    def generate(self, index, res, used_nums, n):
        if index == len(res):
            return True
        if res[index] != 0:
            return self.generate(index + 1, res, used_nums, n)

        for new_n in range(n, 0, -1):
            if used_nums[new_n]:
                continue

            used_nums[new_n] = True
            res[index] = new_n

            if new_n == 1:
                if self.generate(index + 1, res, used_nums, n):
                    return True
            elif (index + new_n < len(res) and res[index + new_n] == 0):
                res[index + new_n] = new_n
                if self.generate(index + 1, res, used_nums, n):
                    return True
                res[index + new_n] = 0
            
            res[index] = 0
            used_nums[new_n] = False
        return False