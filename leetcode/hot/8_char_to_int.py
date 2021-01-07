class Solution:
    def myAtoi(self, s:str) -> int:
        res, flag = 0, 1
        max_, min_= 2**31 - 1, -2**31
        if s == '':
            return 0
        length = len(s)
        for i in range(length):
            while s[i] == ' ' and i < length - 1:
                i += 1
                if i == length - 1:
                    return 0
            if s[i] == '-':
                flag = -1
            if s[i] in '+-' and i < length-1:
                i += 1
            if(s[i] >= '0' and s[i] <= '9'):
                while i < length:
                    if s[i] >= '0' and s[i] <= '9':
                        res = 10*res + int(s[i])
                    else:
                        break
                    if res > max_ and flag == 1:
                        return max_
                    elif res > max_+1 and flag == -1:
                        return min_
                    i += 1
                return flag * res
            else:
                return 0

if __name__ == '__main__':
    obj = Solution()
    print(obj.myAtoi('42'))
    print(obj.myAtoi('-42'))
    print(obj.myAtoi('4193 with words'))
    print(obj.myAtoi('-91283472332'))
    print(obj.myAtoi('words and 987'))
    print(obj.myAtoi('     '))
    print(obj.myAtoi('3.14159'))
    print(obj.myAtoi('+'))
    print(obj.myAtoi(" "))