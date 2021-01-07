# 移除k位数字

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return '0'
        
        stack = []
        for i in range(len(num)):
            while k and stack and num[i] < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(num[i])
        
        print('stack:', stack)
        
        i = 0
        while i < len(stack) and stack[i] == '0':
            i += 1
        res =''
        for j in range(i, len(stack)-k):
            res += stack[j]

        if res == '':
            return '0'
        return res

if __name__ == '__main__':
    obj = Solution()
    print(obj.removeKdigits("1432219", 3))
    print(obj.removeKdigits("10200", 1))
    print(obj.removeKdigits("112", 1))