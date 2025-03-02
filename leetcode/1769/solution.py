class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = [0 for _ in range(len(boxes))]
        balls_to_left = 0
        moves_to_left = 0
        balls_to_right = 0
        moves_to_right = 0

        for i in range(len(ans)):
            ans[i] += moves_to_left
            balls_to_left += int(boxes[i])
            moves_to_left += balls_to_left


            j = len(boxes) - 1 - i
            ans[j] += moves_to_right
            balls_to_right += int(boxes[j])
            moves_to_right += balls_to_right

        return ans