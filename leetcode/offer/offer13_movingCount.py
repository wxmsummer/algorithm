# 机器人的运动范围
class Solution:
    
    # 计算单个数字的数位和
    def digSum(self, x):
        s = 0
        while x != 0:
            s += x % 10
            x = x // 10
        return s
    
    # 计算两个数字的数位和
    def digSum2(self, i, j):
        return self.digSum(i) + self.digSum(j)

    def movingCount(self, m: int, n: int, k: int) -> int:
        # 深度优先
        # (i, j)表示当前位置，x表示当前数位和
        def dfs(i, j, x):
            # 如果超出方格返回0
            if i >= m or j >= n:
                return 0
            # 如果数位和大于k则返回0
            if k < self.digSum2(i, j):
                return 0
            # 如果当前格子已被访问过，返回0
            if (i, j) in visited: 
                return 0
            # 标识当前格子已被访问过
            visited.add((i,j))
            # 开启递归，向右和下走，同时解+1
            return 1 + dfs(i + 1, j, self.digSum2(i+1, j)) + dfs(i, j + 1, self.digSum2(i, j+1))

        visited = set()
        # 代表从 0 0 开始走
        return dfs(0, 0, 0)