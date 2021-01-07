# 翻转单词顺序

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        strs = s.split()
        strs.reverse()
        return ' '.join(strs)


class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        i = j = len(s) - 1
        res = []
        while i >= 0:
            while i >= 0 and s[i] != ' ':
                i -= 1
            res.append(s[i+1:j+1])
            while s[i] == ' ':
                i -= 1
            j = i
        return ' '.join(res)