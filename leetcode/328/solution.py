# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        odd = ListNode(-1)
        even = ListNode(-1)
        curr, oddHead, evenHead = head, odd, even
    
        i = 1
        while curr is not None:
            if i % 2 == 1:
                oddHead.next = curr
                oddHead = oddHead.next
            else:
                evenHead.next = curr
                evenHead = evenHead.next

            curr = curr.next
            i += 1
            
        evenHead.next = None
        oddHead.next = even.next
        
        return odd.next
        