class Solution:
    def maximumSwap(self, n: int) -> int:
        max_digit, max_digit_pos, digit_pos = -1,-1,1
        res, diff = n, 0
        while n > 0:
            curr_digit = n % 10
            if curr_digit > max_digit:
                max_digit = curr_digit
                max_digit_pos = digit_pos
            else:
                diff = max(diff, (max_digit - curr_digit) * (digit_pos - max_digit_pos))
            digit_pos *= 10
            n //= 10

        return res + diff