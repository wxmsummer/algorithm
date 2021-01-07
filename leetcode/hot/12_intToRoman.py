class Solution():
    # 贪心算法，从大到小尝试转换
    def intToRoman(self, num:int) -> str:
        dic = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 
                50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
        roman_digits = []
        for val in dic:
            if num == 0:
                break
            # 计算商和余数
            count, num = divmod(num, val)
            # 将罗马数加到结果上
            roman_digits.append(dic[val] * count)
        return ''.join(roman_digits)
        

if __name__ == '__main__':
    obj = Solution()
    print(obj.intToRoman(11))  