# 二进制中1的个数

class Solution:
    # 采用与运算，诸位&1，然后右移
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n & 1
            n >>= 1
        return res

        