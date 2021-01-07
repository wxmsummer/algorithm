class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        print('decimal:', str(numerator / denominator))

if __name__ == '__main__':
    obj = Solution()
    print(obj.fractionToDecimal(1, 2))
    print(obj.fractionToDecimal(2, 3))
    print(obj.fractionToDecimal(4, 333))