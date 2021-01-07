# 只出现一次的数字：除了一个数字出现一次，其他都出现了三次，找出这个数

# 对于出现三次的数字，各二进制位出现的次数都是3的倍数，对3求余，结果为只出现一次的数字
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = [0] * 32
        for num in nums:
            for j in range(32):
                # 获取二进制最后一位
                counts[j] += num & 1
                # 右移，循环获取num所有位的值
                num >>= 1
        res, m = 0, 3
        # 将counts数组中各二进制位的值恢复到数字res上
        for i in range(32):
            res <<= 1
            res |= counts[31 - i] % m
        # 对于负数要特殊操作
        return res if counts[31] % m == 0 else ~(res ^ 0xffffffff)