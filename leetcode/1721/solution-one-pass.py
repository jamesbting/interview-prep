class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 1
        curr = head
        front = head
        end = None
        while curr is not None:
            if end is not None:
                end = end.next

            if length == k:
                front = curr
                end = head

            length += 1
            curr = curr.next

        temp = front.val
        front.val = end.val
        end.val = temp

        return head