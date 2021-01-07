# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        
        def recur(root, tmp, tar):
            if not root:
                return
            
            tmp.append(root.val)
            if not root.left and not root.right and tar == root.val:
                res.append(tmp[:])

            if root.left:
                recur(root.left, tmp, tar-root.val)
            if root.right:
                recur(root.right, tmp, tar-root.val)
            tmp.pop()
        
        res = []
        recur(root, [], sum)
        return res