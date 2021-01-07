# 最长不含重复字符的子字符串

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic, res, i = {}, 0, -1
        for j in range(len(s)):
            if s[j] in dic: # 如果遇相同的字符
                i = max(dic[s[j]], i) # 更新左指针i的位置
            dic[s[j]] = j
            res = max(res, j-i)
        return res

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        res = count = 0
        for j in range(len(s)):
            # 获取字符s[j] 最近一次出现的下标
            i = dic.get(s[j], -1)
            # 更新字符最近一次出现的下标
            dic[s[j]] = j
            # 如果没遇到重复的，就+1
            if count < j - i:
                count += 1
            # 如果遇到重复的，就变为不算重复字符的长度
            else:
                count = j - i
            res = max(res, count)
        return res


if __name__ == '__main__':
    obj = Solution()
    print(obj.lengthOfLongestSubstring('abcad'))