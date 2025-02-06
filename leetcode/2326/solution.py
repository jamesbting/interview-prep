# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1 for _ in range(n)] for _ in range(m)]
        dx, dy = 0, 1
        x, y = 0, 0
        curr = head

        while curr is not None:
            matrix[x][y] = curr.val
            curr = curr.next
            
            new_x = x + dx
            new_y = y + dy
            if new_x == m or new_y == n or matrix[new_x][new_y] != -1:
                dx, dy = dy, -dx #matrix rotation by 90 degrees
                new_x = x + dx
                new_y = y + dy
            
            x = new_x
            y = new_y        
        

        return matrix

