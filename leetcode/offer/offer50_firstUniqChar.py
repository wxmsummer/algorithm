class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = {}
        for c in s:
            # 若有重复字符，则dic[c]的值为false，否则为true
            dic[c] = not c in dic
        for k, v in dic.items():
            if v: return k
        return ' '

if __name__ == '__main__':
    obj = Solution()
    print(obj.nthUglyNumber(10))