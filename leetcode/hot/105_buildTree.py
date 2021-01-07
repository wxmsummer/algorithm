# 从前序遍历和中序遍历构建二叉树

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: list, inorder: list) -> TreeNode:
        # 如果inorder为空，说明已构建完毕
        if inorder:
            # preorder的第一个元素为根
            value = preorder.pop(0)
            root = TreeNode(value)
            # 找到根节点在中序遍历中的位置
            index = inorder.index(value)
            # 递归构建左右子树
            root.left = self.buildTree(preorder, inorder[:index])
            root.right = self.buildTree(preorder, inorder[index+1:])
            return root