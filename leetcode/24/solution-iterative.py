# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:


        dummy = ListNode(-1)
        dummy.next = head

        prev_node = dummy


        while head and head.next:
            first = head
            second = head.next


            prev_node.next = second
            first.next = second.next
            second.next = first

            prev_node = first
            head = first.next
        return dummy.next
