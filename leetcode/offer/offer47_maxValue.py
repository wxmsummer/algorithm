# 礼物的最大价值

# 设 f(i, j) 为从棋盘左上角走至单元格 (i ,j) 的礼物最大累计价值，
# 易得到以下递推关系：f(i,j) 等于 f(i,j-1) 和 f(i−1,j) 中的较大值加上当前单元格礼物价值 grid(i,j) 

# 将棋盘本身作为dp数组
class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    grid[i][j] += grid[i][j-1]
                elif j == 0:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += max(grid[i][j-1], grid[i-1][j])
            print(grid)
        return grid[-1][-1]
