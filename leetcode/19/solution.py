# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None
        dummy = ListNode(0)
        dummy.next = head
        prev, curr = dummy, dummy

        for i in range(n + 1):
            curr = curr.next 

        while curr is not None:
            curr = curr.next
            prev = prev.next  
        
        #prev points to the node to remove
        prev.next = prev.next.next
        return dummy.next

#pD [1] c 