# 二叉树的最近公共祖先

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 树为空，或者root为p或q，直接返回root
        if not root or root == p or root == q:
            return root
        # 递归遍历左子树，在左子树中寻找p或q，找到谁就返回谁
        left = self.lowestCommonAncestor(root.left, p, q)
        # 递归遍历右子树，在右子树中寻找p或q，找到谁就返回谁
        right = self.lowestCommonAncestor(root.right, p, q)
        # 如果在左子树中找不到p或q，说明p和q都在右子树中
        if not left:
            return right
        # 如果在右子树中找不到p或q，说明p和q都在左子树中
        if not right:
            return left
        # 否则，当left和right均不为空时，说明p和q在root异侧，最近公共祖先即为root
        return root