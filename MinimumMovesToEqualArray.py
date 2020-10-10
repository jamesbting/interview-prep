# https://leetcode.com/problems/minimum-moves-to-equal-array-elements/
# note that incrementing n-1 elements is equivalent to decrementing the largest element
# when we redfine the problem as such, the problem becomes to find how many times we need to decrement an element
# for all the element to be equal
# so adding up all the elements minus the smallest element will give the minimum number of moves
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - (min(nums)*len(nums))
