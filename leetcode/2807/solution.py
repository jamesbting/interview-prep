# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            if prev and curr:
                gcd = self.gcd(max(prev.val, curr.val), min(prev.val, curr.val))
                new_node = ListNode(gcd, curr)

                prev.next = new_node
            prev = curr
            curr = curr.next

        return head
    
    #euclids algo
    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)