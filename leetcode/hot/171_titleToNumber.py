class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        count = len(s)
        for i in range(len(s)):
            res += (ord(s[i]) - ord('A') + 1) * 26**(count-1)
            count -= 1
        return res