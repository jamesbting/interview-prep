class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strings:
            hash_s = self.hash(s)
            ans[hash_s].append(s)

        return list(ans.values())

    def hash_char(self, c, shift):
        return chr((ord(c) - shift) % 26 + ord('a'))

    def hash(self, s):
        shifts = ord(s[0])
        return "".join([self.hash_char(c, shifts) for c in s])