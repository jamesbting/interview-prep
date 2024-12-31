class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        #forward scan: check each prefix for more opens than closes
        opens, closes, right = 0, 0, 0
        res = ""
        while right < len(s):
            c = s[right]
            if c == '(':
                opens += 1
            elif c == ')':
                closes += 1

            if opens >= closes:
                res = res + c
            else:
                closes -= 1
            right += 1

        s = res
        res = ""
        opens, closes = 0, 0
        left = len(s) - 1

        while left >= 0:
            c = s[left]
            if c == '(':
                opens += 1
            elif c == ')':
                closes += 1

            if closes >= opens:
                res = c + res
            else:
                opens -= 1
            left -= 1

        return res