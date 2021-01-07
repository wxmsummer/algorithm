# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 层序遍历，暴力法
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [root]
        count = 0
        while stack:
            node = stack.pop()
            count += 1
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return count

    # 复杂度 O(lgn*lgn)
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        left, right = root.left, root.right
        left_depth, right = 0, 0
        
        # 求左右子树深度
        while left:
            left = left.left
            left_depth += 1
        
        while right:
            right = right.right
            right += 1
        
        # 如果遇到满二叉树
        if left_depth == right:
            return (2 << left_depth) - 1
        
        # 如果不为满二叉树，则节点数量为左子树数量加右子树数量加1，1为自身
        return self.countNodes(root.left) + self.countNodes(root.right) + 1

