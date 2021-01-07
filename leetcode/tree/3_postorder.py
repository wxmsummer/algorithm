# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 左 右 根
    def postorderTraversal(self, root: TreeNode) -> list:
        if not root:
            return []
        
        stack = []
        res = []
        while root or stack:
            if root:
                stack.append(root)
                # 根插入res第一位
                res.insert(0, root.val)
                # 遍历右子树
                root = root.right
            else:
                node = stack.pop()
                # 遍历左子树
                root = node.left

        return res
