# 二叉树的镜像

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 递归解法
class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        def recur(root: TreeNode):
            # dfs，递归地交换左右子树
            if root:
                root.left, root.right = root.right, root.left
                recur(root.left)
                recur(root.right)
            return root

        return recur(root)


# 辅助栈解法
class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        
        stack = [root]
        # 遍历树的所有节点，并交换每个node的左右子树
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            if node.left or node.right:
                node.left, node.right = node.right, node.left

        return root
            
