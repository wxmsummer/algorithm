# 斐波那契数列
class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, (a + b) % 1000000007
        return a 

if __name__ == '__main__':

    obj = Solution()
    print(obj.fib(100))