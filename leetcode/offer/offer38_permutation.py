class Solution:
    def permutation(self, s: str) -> list:
        c = list(s)
        res = []

        def dfs(x):
            # 当前位置到达字符串末尾，将当前排列加入解答
            if x == len(c) - 1: 
                res.append(''.join(c))
                return
            # 用于去除重复方案
            dic = set()
            # 对每个位置x，都进行排列交换
            # 对x到len(c)的每个位置字符，进行交换
            for i in range(x, len(c)):
                if c[i] in dic:
                    continue # 当前字符重复了，不必进行交换，进行剪枝
                dic.add(c[i])
                c[i], c[x] = c[x], c[i] # 交换，将c[i]固定在第x位
                dfs(x+1) # 开启固定第x+1位字符
                c[i], c[x] = c[x], c[i] # 恢复交换，回溯

        dfs(0)
        return res

if __name__ == '__main__':
    
    obj = Solution()
    print(obj.permutation('abc'))