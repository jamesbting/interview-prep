# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        return self.binarySearch(1, n)

    def binarySearch(self, low: int, high: int):
        mid = (low + high) // 2
        mid_guess = guess(mid)

        if(mid_guess == 0):
            return mid
        elif(mid_guess == 1):
            return self.binarySearch(mid + 1, high)
        else:
            return self.binarySearch(low, mid - 1)