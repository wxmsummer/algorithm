# 把数组排成最小的数

import functools

class Solution:
    # 本质上是排序问题
    # 若nums字符串格式x和y
    # 若x + y > y + x 则 m > n
    # 例如 '34' + '30' = 3430 > 3034 = '30' + '34' 
    def minNumber(self, nums: list) -> str:
        # 自己定义排序规则
        def sort_rule(x, y):
            if x+y > y+x:
                return 1
            elif x+y < y+x:
                return -1
            else:
                return 0
        # 将数字转为字符串，再进行字符串排序
        strs = [str(num) for num in nums]
        strs.sort(key=functools.cmp_to_key(sort_rule))
        return ''.join(strs)

if __name__ == '__main__':
    obj = Solution()
    print(obj.minNumber([3,30,34,5,9]))