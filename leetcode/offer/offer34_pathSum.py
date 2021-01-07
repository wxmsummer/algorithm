# 二叉树中和为某一值的路径

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res, path = [], []
        # dfs，回溯法
        def recur(root, tar):
            if not root:
                return
            # 先在path加上当前节点val，然后减去val
            path.append(root.val)
            tar -= root.val
            # 如果正好符合走到叶子节点，且tar为0，说明符合要求，将path加到结果集上
            if tar == 0 and not root.left and not root.right:
                res.append(list(path))
            # 递归左右节点
            recur(root.left, tar)
            recur(root.right, tar)
            # 路径恢复：回溯
            path.pop()

        recur(root, sum)
        return res