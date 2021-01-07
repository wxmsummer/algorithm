# 从上到下打印二叉树

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> list:
        if not root:
            return []

        res = []
        queue = collections.deque()
        queue.append(root)
        # 外层循环，不断将元素入队
        while queue:
            tmp = []
            # 内层循环，将当前层的val加入tmp数组中
            for _ in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(tmp)
        return res
