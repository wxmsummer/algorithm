# 最小路径和

class Solution:
    # 动态规划
    def minPathSum(self, grid: list) -> int:
        row_len, col_len = len(grid), len(grid[0])
        dp = [[0 for i in range(col_len)] for i in range(row_len)]

        # 初始情况
        dp[0][0] = grid[0][0]
        for i in range(1, row_len):
            dp[i][0] += dp[i-1][0] + grid[i][0]

        for j in range(1, col_len):
            dp[0][j] += dp[0][j-1] + grid[0][j]

        # 遍历
        for i in range(1, row_len):
            for j in range(1, col_len):
                print('dp:', dp)
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        
        return dp[row_len-1][col_len-1]

if __name__ == '__main__':
    obj = Solution()
    print(obj.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
    print(obj.minPathSum([[1,2,3],[4,5,6]]))

