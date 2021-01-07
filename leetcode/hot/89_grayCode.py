class Solution:
    def grayCode(self, n: int) -> list:
        if n == 0:
            return [0]
        
        tmp_list = ['0'] * n
        # gray_set用于记录已出现过的格雷码
        gray_set = set()
        
        # 递归求解
        def recur(tmp_list):
            tmp = ''.join(tmp_list)
            # 如果当前格雷码没出现过，就加入解集
            if tmp not in gray_set:
                gray_set.add(tmp)
                res.append(int(tmp, 2))
            # 如果找到所有解，就返回
            if len(res) == 2 ** n:
                return
            # 对当前格雷码，尝试构造出邻接着它的下一个格雷码
            # 具体做法是从低到高去翻转一位
            for i in range(n):
                # 只翻转一位
                tmp_list = reverse(tmp_list, i)
                tmp = ''.join(tmp_list)
                # 如果翻转该位之后可以构成解，则进行递归
                if tmp not in gray_set:
                    recur(tmp_list)
                # 否则，如果翻转某位之后，得到的格雷码已经在集合里，则将该位翻转回来
                # 然后进行下一位的翻转
                else:
                    tmp_list = reverse(tmp_list, i)
        
        # 辅助函数，用于翻转该位数字
        def reverse(tmp_list, idx):
            if tmp_list[idx] == '0':
                tmp_list[idx] = '1'
            else:
                tmp_list[idx] = '0'
            return tmp_list
        
        res = []
        recur(tmp_list)
        return res

if __name__ == '__main__':
    obj = Solution()
    print(obj.grayCode(0))
    print(obj.grayCode(1))
    print(obj.grayCode(2))
    print(obj.grayCode(3))
    print(obj.grayCode(4))