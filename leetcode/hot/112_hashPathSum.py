# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right and sum == root.val:
            return True
        elif not root.left and not root.right and sum != root.val:
            return False
        
        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)
        
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        stack = [(root, sum)]
        while stack:
            node, sum = stack.pop()
            if not node.left and not node.right and sum == node.val:
                return True
            if node.left:
                stack.append((node.left, sum-node.val))
            if node.right:
                stack.append((node.right, sum-node.val))
        return False