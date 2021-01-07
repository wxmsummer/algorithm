# 二叉搜索树的后序遍历序列
# 利用了二叉搜索树的后续遍历序列的特性
# 二叉搜索树 左 < 根 < 右，后序遍历为左右根
# 则先找到根节点就好办了

class Solution:
    def verifyPostorder(self, postorder) -> bool:
        def recur(i, j):
            # 子树节点数量 <= 1，返回true
            # i为左子树起点
            if i > j:
                return True
            p = i
            # 找到第一个大于根节点的节点，划分左右子树
            # postorder[j] 为根节点
            # 左子树区间内所有节点都应该小于根
            while postorder[p] < postorder[j]:
                p += 1
            # m为右子树起点
            m = p
            # 右子树区间内的所有节点都应该大于根
            while postorder[p] > postorder[j]:
                p += 1
            # 遍历到最后，p应该等于j
            # 递归判断左右子树是否符合
            return p == j and recur(i, m-1) and recur(m, j-1)

        return recur(0, len(postorder) - 1)
            