# 不同路径

class Solution:
    # 动态规划 dp[i][j] 表示从(0, 0)走到(i,j)的路径数
    # 由于只能向右或向下，显然，(i, j)的位置可以从(i-1, j) 或 (i, j-1)到达
    # 那么 转移方程： dp[i][j] = dp[i-1][j] + dp[i][j-1]
    # 初始情况：当i为0或j为0时，只有1种路径
    def uniquePaths(self, m:int, n:int) -> int:
        dp = [[0]*n for i in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                # 状态转移方程
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                print('dp:', dp)
        return dp[m-1][n-1]

if __name__ == '__main__':
    obj = Solution()
    print(obj.uniquePaths(3, 4))
