# 剪绳子
import math

# 数学证明
# 任何大于1的数都可由2和3相加组成
# 当n>=5时,将它剪成2或3的绳子段,2(n-2) > n,3(n-3) > n,都大于他未拆分前的情况，
# 当n>=5时，3(n-3) >= 2(n-2),所以我们尽可能地多剪3的绳子段
# 当绳子长度被剪到只剩4时，2 * 2 = 4 > 1 * 3,所以没必要继续剪

class Solution:
    def cuttingRope(self, n: int) -> int:
        if n <= 3: 
            return n - 1

        a = n // 3
        b = n % 3

        if b == 0:
            return int(3 ** a) % 1000000007
        if b == 1:
            return int(3 ** (a-1) * 4) % 1000000007
        
        return int(3 ** a * 2) % 1000000007

if __name__ == '__main__':

    obj = Solution()
    print(obj.cuttingRope(120))