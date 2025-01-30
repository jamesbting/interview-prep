# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 1
        curr = head
        front = head
        while curr is not None:
            length += 1
            curr = curr.next
            if length == k:
                front = curr

        tail = head
        for _ in range(1, length - k):
            tail = tail.next

        temp = front.val
        front.val = tail.val
        tail.val = temp

        return head