# 爬楼梯
# 类似斐波那契数列
# dp[i] = dp[i-1] + dp[i-2]
# 使用a, b 替代 dp数组

class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for i in range(n-1):
            a, b = b, a+b
        
        return b

if __name__ == '__main__':
    obj = Solution()
    print(obj.climbStairs(2))
    print(obj.climbStairs(3))