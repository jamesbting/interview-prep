class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1:
            return False

        open_brackets = 0
        unlocked = 0

        for i in range(len(s)):
            if locked[i] == "0":
                unlocked += 1
            elif s[i] == '(':
                open_brackets += 1
            elif s[i] == ')':
                if open_brackets > 0:
                    open_brackets -= 1
                elif unlocked > 0: 
                    unlocked -= 1
                else:
                    return False

        balance = 0
        for i in range(len(s) - 1, -1, -1):
            if locked[i] == "0":
                balance -= 1
                unlocked -= 1
            elif s[i] == '(':
                open_brackets -= 1
                balance += 1
            elif s[i] == ')':
                balance -= 1
            
            if balance > 0:
                return False
            if unlocked == 0 and open_brackets == 0:
                break

        if open_brackets > 0:
            return False
        return True
