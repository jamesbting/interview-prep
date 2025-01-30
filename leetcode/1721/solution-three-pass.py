# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 1
        curr = head
        while curr is not None:
            length += 1
            curr = curr.next

        tail = head
        for _ in range(1, length - k):
            tail = tail.next

        to_swap = head
        for _ in range(1, k):
            to_swap = to_swap.next

        temp = to_swap.val
        to_swap.val = tail.val
        tail.val = temp

        return head