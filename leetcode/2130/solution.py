# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        vals = []
        curr, i = head, 0
        while curr != None:
            vals.append(curr.val)
            curr = curr.next
            i += 1

        n = len(vals)
        max_sum = 0
        for i in range(0, n // 2):
            max_sum = max(max_sum, vals[i] + vals[n - 1 - i])

        return max_sum