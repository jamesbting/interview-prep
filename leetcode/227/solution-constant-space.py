class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        stack = []
        currentNumber = 0
        lastNumber = 0
        operation = "+"
        result = 0
        for i in range(len(s)):
            c = s[i]
            if c not in {'+', '-', '*', '/'}:
                currentNumber = (currentNumber * 10) + ord(c) - ord('0')
            if c not in {'0', '1', '2', '3', '4', '5', '6','7','8','9'} or i == len(s) - 1:
                if operation == '+':
                    result += lastNumber
                    lastNumber = currentNumber
                elif operation == '-':
                    result += lastNumber
                    lastNumber = - 1 * currentNumber
                elif operation == "*":
                    lastNumber = lastNumber * currentNumber
                elif operation == "/":
                    lastNumber = int(lastNumber / currentNumber)
                operation = c
                currentNumber = 0
        
        return result + int(lastNumber)