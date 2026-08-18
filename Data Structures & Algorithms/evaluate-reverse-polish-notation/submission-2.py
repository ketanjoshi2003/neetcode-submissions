class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i in {'+','-','*','/'}:
                top = stack.pop()
                first = stack.pop()
                if i == '+':
                    stack.append(first + top)

                elif i == '-':
                    stack.append(first - top)
                    
                elif i == '*':
                    stack.append(first * top)
                    
                elif i == '/':
                    stack.append(int(first / top))
            else:
                stack.append(int(i))

        return stack[0]