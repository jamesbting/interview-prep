
class WordDictionary:
    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr["$"] = True
       
            

    def search(self, word: str) -> bool:
        #dfs
        return self.dfs(word, self.root)

    def dfs(self, word, root):
        if root is None:
            return False
        if len(word) == 0:
            return "$" in root
        #keep searching:

        if word[0] == '.':
            for key in root.keys():
                if key != "$" and self.dfs(word[1::], root[key]):
                    return True
            return False
        else:
            return self.dfs(word[1::], root.get(word[0], None))

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)