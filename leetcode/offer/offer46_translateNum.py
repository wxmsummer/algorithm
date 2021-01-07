# 把数字翻译成字符串
# 有点类似青蛙跳台阶

class Solution:
    # 动态规划，设f(i)表示X1X2...X(i-1)Xi的翻译方案数量
    # 若 单独翻译 xi ，则f(i) = f(i-1)
    # 若 X(i-1)Xi 整体可翻译 f(i) = f(i-2) + f(i-1)
    def translateNum(self, num:int) -> int:
        s = str(num)
        a = b = 1
        for i in range(2, len(s)+1):
            temp = a
            if "10" <= s[i-2:i] <= "25":
                a = a+b
            b = temp
        return a

if __name__ == '__main__':
    obj = Solution()
    print(obj.translateNum(12258))
