class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0

        while a > 0 or b > 0 or c > 0:
            a_bit = a % 2
            b_bit = b % 2
            c_bit = c % 2

            if c_bit == 1:
                count += not (a_bit or b_bit)
            else:
                if a_bit == 1 and b_bit == 1:
                    count += 2
                else:
                    count += (a_bit or b_bit)
            a = a // 2
            b = b // 2
            c = c // 2

        return count


        