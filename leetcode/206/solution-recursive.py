# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverseListRecursive(head, None)

    def reverseListRecursive(self, head: Optional[ListNode], prev: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return prev

        next_head = head.next
        head.next = prev

        return self.reverseListRecursive(next_head, head)
