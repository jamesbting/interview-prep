class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1:
            return False

        open_brackets = []
        unlocked = []

        for i in range(len(s)):
            c = s[i]
            if locked[i] == "0":
                unlocked.append(i)
            elif c == '(':
                open_brackets.append(i)
            elif c == ')':
                if len(open_brackets) > 0:
                    open_brackets.pop()
                elif len(unlocked) > 0: 
                    unlocked.pop()
                else:
                    return False

        while len(open_brackets) > 0 and len(unlocked) > 0 and open_brackets[-1] < unlocked[-1]:
            open_brackets.pop()
            unlocked.pop()

        if len(open_brackets) > 0:
            return False
        return True
