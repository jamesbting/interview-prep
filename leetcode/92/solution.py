# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        #find start, find end
        if left == right:
            return head
        prev_start = None
        start = head
        end = head
        i = 1
        while i < left or i< right:
            if i < left:
                prev_start = start
                start = start.next
            if i < right:
                end = end.next
            i += 1
                
        #sever them, and reverse
        if prev_start is not None:
            prev_start.next = None
        next_end = end.next
        if end is not None:
            end.next = None

        reversed_list = self.reverseList(start)

        #rejoin and return head
        if prev_start is not None:
            prev_start.next = reversed_list
        
           
        curr = reversed_list
        while curr.next is not None:
            curr = curr.next
        curr.next = next_end

        return head if prev_start is not None else reversed_list
            

        
       


    def reverseList(self, head):
        curr, prev = head, None

        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev
        