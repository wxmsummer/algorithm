# 数值的整数次方

class Solution:
    # 采用二进制幂的方法
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        res = 1

        if n < 0:
            x = 1/x
            n = -n
        
        # 将次方分解为二进制，然后利用移位，逐步增大乘数
        while n :
            if n & 1:
                res *= x
            x *= x
            n >> 1
        return res