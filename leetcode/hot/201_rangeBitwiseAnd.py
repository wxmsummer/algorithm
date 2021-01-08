class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        res = m
        for i in range(m+1, n+1):
            res &= i
            if res == 0:
                return 0
        return res
