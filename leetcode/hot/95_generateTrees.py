# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> list:
        if n == 0:
            return []
        def build_trees(left, right):
            all_tree = []
            if left > right:
                return [None]
            for i in range(left, right+1):
                # 构造左树
                left_tree = build_trees(left, i-1)
                # 构造右树
                right_tree = build_trees(i+1, right)
                # 
                for l in left_tree:
                    for r in right_tree:
                        cur = TreeNode(i, l, r)
                        all_tree.append(cur)
            return all_tree
        
        res = build_trees(1, n)
        return res

if __name__ == '__main__':
    obj = Solution()
    print(obj.generateTrees(3))