# 树的子结构

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 先序遍历树A，判断A中以nA为根节点的子树是否包含树B
# 时间O(MN)，M，N分别为A，B节点数
# 空间O(M)
class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def recur(A, B):
            # 当B为空，说明树B已匹配完成，返回true
            if not B:
                return True
            # 如果A为空或者A节点和B节点值不相等，返回false
            if not A or A.val != B.val:
                return False
            # 线序，先左子树再右子树
            return recur(A.left, B.left) and recur(A.right, B.right)
        # A，B是否为空  A根节点子树是否包含B， A左子树是否包含B，A右子树是否包含B
        return bool(A and B) and recur(A,B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)