# 去除重复字母

import collections

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        dic = collections.Counter(s)
        stack = []
        for c in s:
            dic[c] -= 1
            if c not in stack:
                while stack and c < stack[-1] and dic[stack[-1]] > 0:
                        stack.pop()
                stack.append(c)
        return ''.join(stack)

if __name__ == '__main__':
    obj = Solution()
    print(obj.removeDuplicateLetters("cbacdcbc"))

