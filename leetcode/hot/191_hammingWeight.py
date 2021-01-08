# 位1的个数

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            # 如果n&1等于1，说明最后一位为1
            if n & 1 == 1:
                count += 1
            # 将n右移一位
            n = n >> 1
        return count