class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []
        self.n = n

        self.backtrack("", 0,0)

        return self.ans

    def backtrack(self, curr, left_count, right_count):
        if len(curr) == 2 * self.n:
            self.ans.append(curr)
            return
        if left_count < self.n:
            self.backtrack(curr + "(", left_count + 1, right_count)
            #curr = curr[:-1]
        if right_count < left_count:
            self.backtrack(curr + ")", left_count, right_count+1)
            #curr = curr[:-1]


# S -> (S)S | empty
  