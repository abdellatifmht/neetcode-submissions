class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}

        for item in tokens:
            if item in operators:
                num1 = stack.pop()
                num2 = stack.pop()

                if item == '+':
                    stack.append(num2 + num1)
                elif item == '-':
                    stack.append(num2 - num1)
                elif item == '*':
                    stack.append(num2 * num1)
                elif item == '/':
                    stack.append(int(num2 / num1))
            else:
                stack.append(int(item))

        return stack[-1]