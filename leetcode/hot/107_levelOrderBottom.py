# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> list:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        res = []
        while queue:
            tmp = []
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(tmp)
        return res.reverse() 