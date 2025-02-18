class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        self.ans = set()
        self.backtrack(tiles, "", [False for _ in tiles])
        return len(self.ans)

    def backtrack(self, tiles, curr, used):
        if all(used):
            return

        for i in range(len(tiles)):
            if used[i]:
                continue
            tile = tiles[i]
            used[i] = True
            new_s = curr + tile

            if new_s not in self.ans:
                self.ans.add(new_s)
                self.backtrack(tiles, new_s, used)

            used[i] = False