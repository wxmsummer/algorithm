# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        # 入两个根节点，便于遍历
        stack = [root, root]
        while stack:
            node1 = stack.pop()
            node2 = stack.pop()
            # 两个node均为空，继续
            if not node1 and not node2:
                continue
            # 其中一个为空，返回False
            if not node2:
                return False
            if not node1:
                return False
            # 值不相等，false
            if node1.val != node2.val:
                return False

            # node1的left和node2的right应该相等
            stack.append(node1.left)
            stack.append(node2.right)
            # node1的right和node2的left应该相等
            stack.append(node1.right)
            stack.append(node2.left)
        # 如果遍历完，没发现False，则True
        return True
