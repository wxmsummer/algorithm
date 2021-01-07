class Solution:
    def sumNums(self, n: int) -> int:
        self.res = 0
        n > 1 and self.sumNums(n-1)
        self.res += n
        return self.res