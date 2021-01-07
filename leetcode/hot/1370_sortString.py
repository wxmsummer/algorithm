class Solution:
    def sortString(self, s:str) -> str:
        if s == '':
            return s
        s_list = list(s)
        s_list.sort()
        res = ''
        s_list = ['#'] + s_list + ['#']
        length = len(s)
        count = 0
        while count < length:
            i = 0
            while i < length+1:
                if s_list[i] != '#' and  s_list[i] != s_list[i+1]:
                    res += s_list[i]
                    s_list[i] = '#'
                    count += 1
                    # print('list:', s_list)
                i += 1
            
            i -= 1
            while i > 0:
                if s_list[i] != '#' and  s_list[i] != s_list[i-1]:
                    res += s_list[i]
                    s_list[i] = '#'
                    count += 1
                    # print('list:', s_list)
                i -= 1
        
        return res

class Solution:
    def sortString(self, s: str) -> str:
        num = [0] * 26
        for ch in s:
            num[ord(ch) - ord('a')] += 1
        
        ret = list()
        while len(ret) < len(s):
            for i in range(26):
                if num[i]:
                    ret.append(chr(i + ord('a')))
                    num[i] -= 1
            for i in range(25, -1, -1):
                if num[i]:
                    ret.append(chr(i + ord('a')))
                    num[i] -= 1

        return "".join(ret)


if __name__ == '__main__':
    obj = Solution()
    print(obj.sortString('leetcode'))
    print(obj.sortString('aaaabbbbcccc'))


# 抖音火山小视频
# 用户技术体验，网络优化，后端架构，播放引擎
# 用户上传视频到用户消费
# 
# 
# 
# 
# 
# 
# 
# 