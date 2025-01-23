class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        stack = []
        currentNumber = ""
        operation = "+"
        for i in range(len(s)):
            c = s[i]
            if c not in {'+', '-', '*', '/'}:
                currentNumber += c
            if c not in {'0', '1', '2', '3', '4', '5', '6','7','8','9'} or i == len(s) - 1:
                if operation == '+':
                    stack.append(int(currentNumber))
                elif operation == '-':
                    stack.append(-1 * int(currentNumber))
                elif operation == "*":
                    number = stack.pop()
                    stack.append(number * int(currentNumber))
                elif operation == "/":
                    number = stack.pop()
                    stack.append(int(number / int(currentNumber)))
                operation = c
                currentNumber = ""
        
        return sum(stack)