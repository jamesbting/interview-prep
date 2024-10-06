class Solution:
    letter_map = {
        2: ['a', 'b' ,'c'],
        3: ['d', 'e' ,'f'],
        4: ['g', 'h' ,'i'],
        5: ['j', 'k' ,'l'],
        6: ['m', 'n' ,'o'],
        7: ['p', 'q' ,'r', 's'],
        8: ['t', 'u' ,'v'],
        9: ['w', 'x' ,'y', 'z']
    }
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        self.letterCombinationsWithAns(digits, ans, "")
        return ans

    def letterCombinationsWithAns(self, digits: str, ans: List[str], prefix: str) -> None:
        if len(digits) == 0:
            if prefix != "":
                ans.append(prefix)
            return
        
        digit = int(digits[0])
        for letter in self.letter_map[digit]:
            self.letterCombinationsWithAns(digits[1:], ans, prefix + letter)



    