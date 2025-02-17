class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        char_count = [0 for _ in range(26)]
        for tile in tiles:
            char_count[ord(tile) - ord('A')] += 1

        return self.backtrack(char_count)
    def backtrack(self, char_count):
        total = 0

        for i in range(26):
            if char_count[i] == 0:
                continue

            total += 1
            char_count[i] -= 1
            total += self.backtrack(char_count)
            char_count[i] += 1
        return total