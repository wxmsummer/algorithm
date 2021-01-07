class Solution():
    # 直接遍历，逐个翻译
    def romanToInt(self, s:str) -> int:
        # 由大到小构造罗马字字典
        dic = {'M':1000, 'CM':900, 'D':500, 'CD':400, 'C':100, 'XC':90, 
                'L':50, 'XL':40, 'X':10, 'IX':9, 'V':5, 'IV':4, 'I':1}     
        tmp, res = '', 0
        if not s:
            return 0
        i = 0
        # 遍历字符串
        while i < len(s):
            # tmp表示可能构成的罗马字符，如果tmp不在字典中，则继续拼下一个罗马字符
            if i < len(s) - 1:
                # 往前预先判断是否能构成2字符罗马字
                tmp = s[i] + s[i+1]
            if tmp in dic:
                res += dic[tmp]
                # 构成两字符罗马字，i往前走2步
                i += 2
                tmp = ''
            else:
                res += dic[s[i]]
                # 不是两字符罗马数字，i往前走1步
                i += 1
        return res

if __name__ == '__main__':
    obj = Solution()
    print(obj.romanToInt('IV'))