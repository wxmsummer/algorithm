# 青蛙跳台阶问题
class Solution:
    def numWays(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n):
            a, b = b, (a + b) % 1000000007
        return a 

if __name__ == '__main__':

    obj = Solution()
    print(obj.numWays(100))