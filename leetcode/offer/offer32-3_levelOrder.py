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
        # 使用count来标记当前层数是奇数还是偶数
        count = 1
        while queue:
            tmp = collections.deque()
            # 内层循环，将每一层的元素加入tmp数组中
            for _ in range(len(queue)):
                node = queue.popleft()
                # 如果为偶数层，就往左加
                if count %2 == 0:
                    tmp.appendleft(node.val)
                # 奇数层，正常添加
                else:
                    tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            count += 1
            res.append(list(tmp))
        return res