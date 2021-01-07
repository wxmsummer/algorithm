# 只出现一次的数字：除了两个数字出现一次，其他都出现了两次，找出这两个数

# 分组法 + 位运算
class Solution:
    def singleNumbers(self, nums: list) -> list:
        ret, a, b = 0, 0, 0
        # 先计算所有数字异或结果
        for num in nums:
            ret ^= num
        h = 1
        print('ret:', ret)
        # 找出ret中不为零的那个位置
        while(ret & h == 0):
            h <<= 1
        # 用该不为零的位置去区分这两个数，以及其所属的组
        for num in nums:
            if h & num == 0:
                a ^= num
            else:
                b ^= num
        
        return [a, b]

if __name__ == '__main__':
    obj = Solution()
    print(obj.singleNumbers([1, 2, 5, 2]))