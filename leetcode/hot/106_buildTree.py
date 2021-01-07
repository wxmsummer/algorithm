# 从后序遍历和中序遍历构建二叉树

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: list, postorder: list) -> TreeNode:
        # 如果inorder为空，说明已构建完毕
        if inorder:
            # postorder的第一个元素为根
            value = postorder.pop()
            root = TreeNode(value)
            # 找到根节点在中序遍历中的位置
            index = inorder.index(value)
            # 递归构建左右子树
            # 注意这里需要先构建右子树，再构建左子树
            root.right = self.buildTree(inorder[index+1:], postorder)
            root.left = self.buildTree(inorder[:index], postorder)
            return root