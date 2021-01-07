class Solution:
    def isValidBST(self, root:TreeNode) -> bool:
        # 判断以node为根节点的子树，其子树中所有的值是否都在(low, up)范围内
        def helper(node, low = flaot('-inf'), up = float('inf')):
            if not node:
                return True
            val = node.val
            # 如果
            if val <= low or val >= up:
                return False
            # 判断右子树的值是否都大于val
            if not helper(node.right, val, up):
                return False
            # 判断左子树的值是否都小于lval
            if not helper(node.left, low, val):
                return False
            return True
        return helper(root)


    def isValidBST(self, root:TreeNode) -> bool:
        stack = []
        p = root
        # pre 记录当前节点的前一节点，用于数据比较
        pre = None
        while p or stack:
            print('p:', p)
            # 先往左
            while p:
                stack.append(p)
                p = p.left
            p = stack.pop()
            # 进行判断
            if pre and root.val <= pre.val:
                return False
            # 
            pre = p
            p = p.right
        return True