class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, i, j):
            grid[i][j] = 0
            rows, cols = len(grid), len(grid[0])
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= x < rows and 0 <= y < cols and grid[x][y] == '1':
                    dfs(grid, x, y)
        
        n = len(grid)
        if n == 0:
            return 0
        
        nc = len(grid[0])
        count = 0
        for i in range(n):
            for j in range(nc):
                if grid[i][j] == "1":
                    count += 1
                    dfs(grid, i, j)
        return count
    
    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        
        nc = len(grid[0])

        count = 0
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == '1':
                    count += 1
                    grid[i][j] = '0'
                    q = collections.deque([(i,j)])
                    while q:
                        for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == '1':
                                q.append((x,y))
                                grid[x][y] == '0'
        return count