# 从上到下打印二叉树

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 层序遍历，借助队列的先入先出实现
    def levelOrder(self, root: TreeNode) -> list:
        if not root:
            return []

        res = []
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return res

class Solution:
    def levelOrder(self, root: TreeNode) -> list:
        if not root:
            return []

        queue, res = [root], []
        while queue:
            node = queue[0]
            queue = queue[1:]
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res

