# 二叉树的深度

# 递归解法 树的深度等于左子树深度与右子树深度最大值+1
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


# 层序遍历 使用队列实现
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue, res = [root], 0
        while queue:
            tmp = []
            for node in queue:
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            queue = tmp
            res += 1
        return res