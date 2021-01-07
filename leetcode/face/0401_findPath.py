from collections import defaultdict
# import collections
# class Solution:
#     def findWhetherExistsPath(self, n:int, graph:list, start:int, target:int) -> bool:
#         # 邻接表，存储图
#         link_table = [set() for _ in range(n)]
#         # 遍历图，存储进邻接表中
#         for i, j in graph:
#             link_table[i].add(j)
#             # print('link_table:', link_table)
#         # 使用visited数组表示是否遍历过当前节点的所有邻接节点
#         visited = [0] * n

#         # 双端队列，用于遍历
#         deque = collections.deque([start])
#         while deque:
#             # print('deque:', deque)
#             cur_node = deque.popleft()
#             # 说明存在通路
#             if target in link_table[cur_node]:
#                 return True
#             # 遍历cur_node的所有邻接节点
#             for node in link_table[cur_node]:
#                 # 如果某节点未遍历过，则将其加入queue，下次遍历其邻接节点
#                 if visited[node] == 0:
#                     deque.append(node)
#             # 表示已访问完当前node的所有邻接节点
#             visited[cur_node] = 1
#         return False

class Solution:
    def findWhetherExistsPath(self, n:int, graph:list, start:int, target:int) -> bool:
        # 使用字典存储邻接表
        link_table = defaultdict(set)
        for k, v in graph:
            link_table[k].add(v)
            print('link_table:', link_table)
        
        # 深度优先
        def dfs(start, target, visited):
            print('start:', start)
            if start == target:
                return True
            # 如果当前节点已经被访问过，则返回false
            if visited[start]:
                print('visited[start]:', start)
                return False
            # 标记当前节点已被访问
            visited[start] = True
            judge = False
            # 开启深度优先
            if start in link_table:
                # 对当前节点的所有邻接节点都进行深度优先
                for cur in link_table[start]:
                    print('cur:', cur)
                    # 将判断结果传递到judge中
                    judge = judge or dfs(cur, target, visited)
            return judge

        visited = [False] * n
        return dfs(start, target, visited)

if __name__ == '__main__':
    obj = Solution()
    print(obj.findWhetherExistsPath(n = 7, graph = [[0, 1], [0, 2], [1, 2], [1, 3], [2, 1], [2, 3], [3, 2], [4, 5], [5, 6]], start = 0, target = 4))
