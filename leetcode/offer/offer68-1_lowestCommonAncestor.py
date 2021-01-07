# 二叉搜索树的最近公共祖先

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 巧妙地利用了二叉搜索树的性质：左小右大
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            # 说明p，q在root的右子树
            if root.val < p.val and root.val < q.val:
                root = root.right
            # 说明p，q在root的左子树
            elif root.val > p.val and root.val > q.val:
                root = root.left
            else:
                break
        return root