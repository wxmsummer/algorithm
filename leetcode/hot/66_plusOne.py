class Solution:
    def plusOne(self, digits: list) -> list:
        digits = [0] + digits
        length = len(digits)
        digits[length-1] += 1
        i = length - 1
        while i > 0:
            digits[i-1] += digits[i] // 10
            digits[i] %= 10 
            i -= 1

        if digits[0] == 0:
            digits = digits[1:]

        return digits

if __name__ == '__main__':
    obj = Solution()
    print(obj.plusOne([1,2,3]))
    print(obj.plusOne([1,9,9]))
    print(obj.plusOne([9]))