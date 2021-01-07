
class Solution():
    def compress(self, s):
        num, string = '', ''
        strStack, numStack = [], []
        for i in range(len(s)):
            if s[i] == '[':
                strStack.append(string)
                string = ''
            elif s[i] == ']':
                temp_num = int(numStack.pop())
                temp_str = strStack.pop()
                while temp_num > 0:
                    temp_str += string
                    temp_num -= 1
                string = temp_str
            elif s[i] == '|':
                numStack.append(int(num))
                num = ''
            elif s[i] >= '0' and s[i] <= '9':
                num += s[i]
            else:
                string += s[i]
            print('strStack:', strStack, 'numStack:', numStack)
        return string


if __name__ == '__main__':
    obj = Solution()
    # obj.compress('HG[3|B[2|CA]]F')
    # print(obj.compress('A[2|CR]D[3|EJ]F'))
    print(obj.compress('BHCJSBCSCW[100|DASKDNKJWDNWCNQWCNOQCNQWOICNWQOINCWQOICNQWOIXWOISWIODAOWPQWDMQKOQZCDWF]WQJDWQUINCQQW[99|SDWQJCIQIUWCNQUCNWQIDNWQUIFNSALQP]DQOJOIXZALPPQQAAX'))