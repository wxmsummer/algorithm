class Codec:
    # 序列化 直接层序遍历
    def serialize(slef, root):
        if not root:
            return "[]"
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("null")
        return '[' + ','.join(res) + ']'

    def deserialize(self, data):
        if data == '[]':
            return
        vals = data[1:-1].split(',')
        i = 1
        root = TreeNode(int(vals[0]))
        queue = collections.deque()
        # 将root加入queue
        queue.append(root)
        # 循环，使用队列
        while queue:
            node = queue.popleft()
            # 构建左节点，跳过null
            if vals[i] != 'null':
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            # 构建右节点，跳过null
            if vals[i] != 'null':
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1
        return root