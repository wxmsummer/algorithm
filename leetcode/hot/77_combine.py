# 组合

class Solution:
    def combine(self, n: int, k: int) -> list:
        # 回溯法，idx为当前元素，cur为当前解
        def backtrack(idx, cur):
            # 如果当前解符合要求，就加入解集
            if len(cur) == k:
                res.append(cur[:])
            # 遍历当前位置后面的元素
            for i in range(idx, n+1):
                print('cur:', cur)
                cur.append(i)
                # 开启下一层判断
                backtrack(i+1, cur)
                # 回溯
                cur.pop()
        res = []
        # 注意这里是从1开始
        backtrack(1, [])
        return res

if __name__ == '__main__':
    obj = Solution()
    print(obj.combine(4, 3))