# 逆波兰表达式求值

class Solution:
    def evalRPN(self, tokens: list) -> int:
        if not tokens:
            return 0
        length = len(tokens)
        num_stack = []
        i = 0
        while i < length:
            if tokens[i] not in '+-*/':
                num_stack.append(int(tokens[i]))
            else:
                num1 = num_stack.pop()
                num2 = num_stack.pop()
                if tokens[i] == '+':
                    num_stack.append(num1 + num2)
                elif tokens[i] == '-':
                    num_stack.append(num2 - num1)
                elif tokens[i] == '*':
                    num_stack.append(num1 * num2)
                elif tokens[i] == '/':
                    num_stack.append(int(num2 / num1))
            i += 1
        return num_stack.pop()

if __name__ == '__main__':
    print('6 // -132:', int(6 / -132))