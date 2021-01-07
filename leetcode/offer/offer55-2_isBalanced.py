# 判断二叉树是否平衡

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 对二叉树做后序遍历，自底向上返回子树深度，若判定某子树不平衡则直接返回
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # 若平衡，则返回当前子树最大深度，否则返回-1表示不平衡
        def recur(root):
            if not root:
                return 0
            left = recur(root.left)
            if left == -1:
                return -1
            right = recur(root.right)
            if right == -1:
                return -1
            return max(left, right) + 1 if abs(left - right) <= 1 else -1
        
        return recur(root) != -1

# 递归解法，逐层判断
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        return (abs(self.depth(root.left) - self.depth(root.right)) <= 1) and self.isBalanced(root.left) and self.isBalanced(root.right)

    # 表示以root为根的树的高度
    def depth(self, root):
        if not root:
            return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1