class Solution:
    def reverseBits(self, n: int) -> int:
        ret, power = 0, 31
        while n:
            # n & 1 确认最右位是不是1，然后左移power位
            ret += (n & 1) << power
            # n右移一位，继续取n最右位，同时power-1
            n = n >> 1
            power -= 1
        return ret