class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colored_balls = {}
        color_count = {}
        ans = []
        for ball, color in queries:
            
            if ball in colored_balls:
                color_count[colored_balls[ball]] -= 1
                if color_count[colored_balls[ball]] <= 0:
                    color_count.pop(colored_balls[ball])
                colored_balls.pop(ball)
            
            colored_balls[ball] = color
            color_count[color] = color_count.get(color, 0) + 1

            ans.append(len(color_count.keys()))
        return ans