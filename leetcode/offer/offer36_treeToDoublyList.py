# 二叉搜索树与双向链表

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        # 中序遍历
        def dfs(cur):
            if not cur:
                return
            # 递归左子树
            dfs(cur.left)
            # 修改节点引用
            if self.pre:
                self.pre.right = cur
                cur.left = self.pre
            else: # 记录头节点
                self.head = cur
            # 保存cur
            self.pre = cur
            # 递归右子树
            dfs(cur.right)

        if not root:
            return
        self.pre = None
        dfs(root)
        
        # 修改首尾指向
        self.head.left = self.pre
        self.pre.right = self.head
        
        return self.head

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':

