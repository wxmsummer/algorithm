class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        
        count = 0
        for i in range(2, n):
            if self.isPrimes(i):
                count += 1
        return count

    def isPrimes(self, n:int) -> bool:
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True

    def countPrimes(self, n: int) -> int:
        isPrimes = [1] * n
        count = 0
        for i in range(2, n):
            if isPrimes[i] == 1:
                count += 1
            j = i
            while i * j < n:
                isPrimes[i * j] = 0
                j += 1
        return count

if __name__ == '__main__':
    obj = Solution()
    print(obj.countPrimes(10))