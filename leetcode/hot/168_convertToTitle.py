class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ''
        while n > 0:
            n -= 1
            n, b = n // 26, n % 26
            res = chr(b + 65) + res
            
        return res
    
if __name__ == '__main__':
    obj = Solution()
    print(obj.convertToTitle(1))
    print(obj.convertToTitle(26))
    print(obj.convertToTitle(28))
    print(obj.convertToTitle(701))
    print(obj.convertToTitle(52))