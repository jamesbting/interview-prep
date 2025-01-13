class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        stack = []
        toRemove = [False for _ in range(n)]

        for i in range(n):
            asteroid = asteroids[i]
            if asteroid > 0:
                stack.append(i)
            elif asteroid < 0:
                while len(stack) > 0:
                    if abs(asteroid) > asteroids[stack[-1]]:
                        toRemove[stack.pop()] = True
                    elif abs(asteroid) < asteroids[stack[-1]]:
                        toRemove[i] = True
                        break
                    else:
                        toRemove[i] = True
                        toRemove[stack.pop()] = True
                        break
        
        ans = []
        for i in range(n):
            if not toRemove[i]:
                ans.append(asteroids[i])
        return ans

