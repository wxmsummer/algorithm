# 省份数量

from typing import List

class Solution:
    # 广度优先：遍历所有城市， 对每一个城市，如果该城市尚未被访问过，则从该城市开始进行深度优先搜索
    # 通过isConnected判断与该城市直接相连的城市有哪些，这些城市与该城市属于同一个连通分量
    # 然后对这些城市继续深度优先搜索，直到同一个连通分量的所有城市都被访问到，即可得到一个省份
    # 遍历完所有城市之后，即可得到连通分量的总数，即省份的总数
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i:int):
            for j in range(n):
                if isConnected[i][j] == 1 and j not in visited:
                    visited.add(j)
                    dfs[j]
        
        n = len(isConnected)
        visited = set()
        count = 0

        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        
        return count
        
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        count = 0

        for i in range(count):
            if i not in visited:
                q = collections.deque([i])
                while q:
                j = q.popleft()
                visited.add(j)
                for k in range(n):
                    if isConnected[i][j] == 1 and k not in visited:
                        q.append(k)
                count += 1
        return count
