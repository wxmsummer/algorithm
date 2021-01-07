from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(int)
        visited = set()
        for i in range(len(equations)):
            a, b = equations[i]
            graph[(a,b)] = values[i]
            graph[(b,a)] = 1/values[i]
            visited.add(a)
            visited.add(b)

        arr = list(visited)
        # 暴力 三倍遍历
        for k in arr:
            for i in arr:
                for j in arr:
                    if graph[(i, k)] and graph[(k, j)]:
                        graph[(i, j)] = graph[(i, k)] * graph[(k, j)]
        res = []
        for x, y in queries:
            if graph[(x, y)]:
                res.append(graph[(x, y)])
            else:
                res.append(-1)
        return res