# 有效的字母异位词

from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = defaultdict(int)
        for i in s:
            dic[i] += 1
        for j in t:
            dic[j] -= 1
        for val in dic.values():
            if val != 0:
                return False
        return True

if __name__ == '__main__':
    obj = Solution()
    print(obj.isAnagram('anagram', 'nagaram'))
    print(obj.isAnagram('rat', 'car'))