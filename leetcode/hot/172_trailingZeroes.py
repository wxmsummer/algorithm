class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        # 从5开始，计算因子5的个数
        for i in range(5, n+1, 5):
            while i % 5 == 0:
                count += 1
                i //= 5
        return count