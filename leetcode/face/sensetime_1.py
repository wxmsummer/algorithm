class Solution:
    def func(self, s) -> int:
        num_stack, symbol_stack = [], []
        if s == '':
            return 0
        i = 0
        while i < len(s):
            # print('num_stack:', num_stack)
            # print('symbol_stack:', symbol_stack)
            if s[i] >= '0' and s[i] <= '9':
                num_stack.append(s[i])
            elif s[i] in '+-':
                symbol_stack.append(s[i])
            elif s[i] in '*/':
                if s[i] == '*':
                    num = int(num_stack.pop())
                    num_stack.append(int(s[i+1]) * num)
                    i += 1
                else:
                    num = int(num_stack.pop())
                    num_stack.append(int(s[i+1]) / num)
                    i += 1
            i += 1
        
        while symbol_stack:
            # print('num_stack:', num_stack)
            # print('symbol_stack:', symbol_stack)
            symbol = symbol_stack.pop()
            if symbol == '+':
                num1 = int(num_stack.pop())
                num2 = int(num_stack.pop())
                num_stack.append(num1 + num2)
            elif symbol == '-':
                num1 = int(num_stack.pop())
                num2 = int(num_stack.pop())
                num_stack.append(num2 - num1)

        return num_stack.pop()

if __name__ == '__main__':
    obj = Solution()
    print(obj.func('1+2*3+4'))

# 理论课 操作系统 网络 需要加强
# 实践比较熟练