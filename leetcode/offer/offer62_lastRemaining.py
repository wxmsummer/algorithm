# 圆圈中最后剩下的数字（约瑟夫环）

# 数学解法，迭代
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        f = 0
        for i in range(2, n+1):
            f = (m + f) % i
        return f

# 递归解法
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        return recur(n, m)

    def recur(self, n, m):
        if n == 0:
            return 0
        # x为对长度n-1的序列，留下的元素
        x = recur(n-1, m)
        # (m%n + x)%n = (m+x)%n
        return (m+x) % n