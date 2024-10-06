# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
            ### find halfway point
            slow, fast = head, head
            while fast != None and fast.next != None:
                slow = slow.next
                fast = fast.next.next

            ## reverse linked list
            reversedHalf = self.reverseLinkedList(slow)

            ##move start and halfway pointers and find max sum
            curr = head
            ans = 0
            while reversedHalf != None:
                ans = max(ans, curr.val + reversedHalf.val)
                curr = curr.next
                reversedHalf = reversedHalf.next
    

            return ans

    
    def reverseLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev