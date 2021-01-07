# 二叉搜索树的第k大节点

# 中序遍历的倒序：右 根 左 为递减序列
# 遍历到中序遍历倒序的第k个节点即为解
class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def dfs(root):
            if not root:
                return
            dfs(root.right)
            if self.k == 0:
                return
            self.k -= 1
            if self.k == 0:
                self.res = root.val
            dfs(root.left)

        self.k = k
        dfs(root)
        return self.res