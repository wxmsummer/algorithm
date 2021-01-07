# 复杂链表的复制

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # 深度优先
        def dfs(temp):
            if not temp:
                return None
            if temp in visited:
                return visited[temp]
            # 创建一个新的节点
            copy = Node(temp.val, None, None)
            # 标记该temp节点已被拷贝过，下次有random指向的时候不会重复拷贝
            visited[temp] = copy
            # 递归拷贝head的next节点和random节点
            copy.next = dfs(temp.next)
            copy.random = dfs(temp.random)
            return copy
        visited = {}
        return dfs(head)

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        visited = {}
        def getCloneNode(node):
            if node:
                if node in visited:
                    return visited[node]
                else:
                    visited[node] = Node(node.val, None, None)
                    return visited[node]
            return node

        if not head:
            return head
        old_node = head
        new_node = Node(old_node.val, None, None)
        visited[old_node] = new_node

        while old_node:
            new_node.next = getCloneNode(old_node.next)
            new_node.random = getCloneNode(old_node.random)

            old_node = old_node.next
            new_node = new_node.next
        return visited[head]
