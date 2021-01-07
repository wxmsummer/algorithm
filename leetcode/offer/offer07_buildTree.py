# 重建二叉树

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.dic = {}
        self.po = preorder
        # 记录中序遍历元素对应下标，便于划分左右子树
        for i in range(len(inorder)):
            self.dic[inorder[i]] = i
        return self.recur(0, 0, len(inorder) - 1)

    # 递归，pre_root 为前序遍历中根节点索引，in_left为中序遍历中左边界，in_right为中序遍历右边界
    def recur(self, pre_root, in_left, in_right):
        # in_left > in_right 说明子树中序遍历为空，已越过叶子节点，返回null
        if in_left > in_right:
            return
        # 根节点
        root = TreeNode(self.po[pre_root])
        # 根节点在中序遍历中的下标
        i = self.dic[self.po[pre_root]]
        # 开启
        root.left = self.recur(pre_root + 1, in_left, i-1)
        root.right = self.recur(i - in_left + pre_root + 1, i + 1, in_right)
        return

def buildTree(self, preorder, inorder):
    if inorder:
        # 确定根节点的下标
        index = inorder.index(preorder.pop(0))
        # 新建node
        root = TreeNode(inorder[index])
        # 递归创建左子树，
        root.left = self.buildTree(preorder, inorder[0:index])
        # 递归创建右子树
        root.right = self.buildTree(preorder, inorder[index+1:])
        return root

