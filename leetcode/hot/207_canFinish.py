class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 边的表示 使用字典保存和该点相连的边
        edges = collections.defaultdict(list)
        # 各个点的入度 初始化都为零
        indeg = [0] * numCourses

        # 计算每个点都指向了哪些边
        # 更新每个点的入度数量
        for info in prerequisites:
            edges[info[1]].append(info[0])
            indeg[info[0]] += 1

        # 将入度为0的节点都入队
        q = collections.deque()
        for u in range(numCourses):
            if indeg[u] == 0:
                q.append(u) 

        visited = 0

        # 从队列中出队
        while q:
            visited += 1
            u = q.popleft()
            # 出队之后，更新该节点指向的其他节点的入度，减去1
            for v in edges[u]:
                indeg[v] -= 1
                # 如果更新的时候发现了新的0入度节点 就将入队
                if indeg[v] == 0:
                    q.append(v)

        return visited == numCourses