class Solution:
    def nextGreaterElement(self, n: int) -> int:

        digits = [int(s) for s in str(n)]
        i = len(digits) - 2
        while i >= 0 and digits[i + 1] <= digits[i]:
            i -= 1

        if i < 0:
            return -1

        j = len(digits) - 1
        while j >= 0 and digits[j] <= digits[i]:
            j -= 1
        
        tmp = digits[i]
        digits[i] = digits[j]
        digits[j] = tmp

        reversed_digits = digits[i + 1:]
        reversed_digits.reverse()
        digits = digits[:i + 1] + reversed_digits


        ans = int(''.join(map(str, digits)))
        return -1 if ans > (2 ** 31 - 1) or ans == n else ans



#3415