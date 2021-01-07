
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 递归解法
    def inorderTraversal(self, root:TreeNode) -> list:
        res = []
        def recur(root:TreeNode):
            if root:
                recur(root.left)
                res.append(root.val)
                recur(root.right)
        recur(root)
        return res

    # 迭代解法
    # 建议使用纸笔模拟入栈出栈过程
    def inorderTraversal(self, root:TreeNode) -> list:
        res = []
        # 创建一个stack用于存放迭代时的节点
        stack = []
        # 空树直接返回
        if not root:
            return []
        # 先将根节点放入stack
        stack.append(root)
        # 不断往栈中添加节点
        cur = root
        while stack:
            # 优先添加左树
            while(cur.left):
                stack.append(cur.left)
                cur = cur.left
            # 取出node，添加val
            node = stack.pop()
            res.append(node.val)
            # 如果node有右子树，就添加右子树
            if node.right:
                stack.append(node.right) 
                # 更新cur，以便接下来继续优先添加左子树
                cur = node.right 
        return res

if __name__ == '__main__':
    obj = Solution()
    print(obj.inorderTraversal(root))