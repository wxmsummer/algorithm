# 二叉树的右视图

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from typing import List
from collections import deque
class Solution:
    # 层序遍历 每一层的最后一个元素 即为右视图元素
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        q = collections.deque()
        q.append(root)
        res = []
        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if i == n - 1:
                    res.append(node.val)
        return res
