# 对称的二叉树

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # 从顶至底递归，判断每对节点是否对称
        def recur(L, R):
            # 如果左右子树均为空，返回true
            if not L and not R:
                return True
            # 如果左右不对称，返回false
            if not L or not R or L.val != R.val:
                return False
            # 递归判断L的左子树和R的右子树是否对称
            # 且判断L的右子树和R的左子树是否对称
            return recur(L.left, R.right) and recur(L.right, R.left)
        # 空树返回true
        if not root :
            return True
        
        # 开启递归判断
        return recur(root.left, root.right)
            