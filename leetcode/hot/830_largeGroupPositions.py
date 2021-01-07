from typing import List

class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        start, end = 0, 0
        length = 0
        res = []
        while end < len(s):
            while end < len(s) and s[end] == s[start]:
                length = end - start + 1
                end += 1
            if length >= 3:
                res.append([start, end-1])
            start = end

        return res

if __name__ == '__main__':
    obj = Solution()
    print(obj.largeGroupPositions("abcxxxxzzy"))
    print(obj.largeGroupPositions("abc"))
    print(obj.largeGroupPositions("abcdddeeeeaabbbcd"))