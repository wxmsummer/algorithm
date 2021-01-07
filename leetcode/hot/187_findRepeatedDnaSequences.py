from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        seen = set()
        res = set()
        for i in range(n - 9):
            # print('seen:', seen)
            cur = s[i:i+10]
            if cur in seen:
                res.add(cur)
            else:
                seen.add(cur)
        return list(res)

if __name__ == '__main__':
    obj = Solution()
    print(obj.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
    print(obj.findRepeatedDnaSequences("AAAAAAAAAAAAA"))
    print(obj.findRepeatedDnaSequences("AAAAAAAAAAA"))

