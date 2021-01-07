
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 递归解法
    def preorderTraversal(self, root:TreeNode) -> list:
        res = []
        def recur(root:TreeNode):
            if root:
                res.append(root.val)
                recur(root.left)
                recur(root.right)
        recur(root)
        return res

    # 迭代解法
    def preorderTraversal(self, root:TreeNode) -> list:
        res = []
        # 创建一个stack用于存放迭代时的节点
        stack = []
        # 先将根节点放入stack
        stack.append(root)
        # 不断往栈中添加节点
        while stack:
            print('stack:', stack)
            print('res:', res)
            node = stack.pop()
            if node:
                res.append(node.val)
                # 这里为什么是先加右子树：是因为栈的先入后出属性
                # 所以先放入右节点，这样出栈的时候就是 先左再右
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        return res

if __name__ == '__main__':
    obj = Solution()
    print(obj.preorderTraversal(root))