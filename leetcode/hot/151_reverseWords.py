# 翻转字符串里的单词

class Solution:
    def reverseWords(self, s: str) -> str:
        s.replace(' ', '')
        sList = s.split()
        sList.reverse()
        return ' '.join(sList)