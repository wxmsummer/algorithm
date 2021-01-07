# 字母异位词分组
class Solution:
    # 将单词转换为列表后按字典序排序
    # 使用dic保存分组
    def groupAnagrams(self, strs:list) -> list:
        dic = {}
        length = len(strs)
        for i in range(length):
            l = list(strs[i])
            l.sort()
            s = ''.join(l)
            if s in dic:
                dic[s].append(strs[i])
            else:
                dic[s] = [strs[i]]
        res =[]
        for val in dic.values():
            res.append(val)

        return res

if __name__ == '__main__':
    obj = Solution()
    print(obj.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
