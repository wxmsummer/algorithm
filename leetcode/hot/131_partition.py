# 分割回文串

class Solution:
    def partition(self, s: str) -> list:
        
        if s == '':
            return []

        # 递归+回溯，分割字符串
        def recur(start, subset):
            if start == len(s):
                res.append(subset[:])
                return
            for i in range(start, len(s)):
                if not helper(s[start:i+1]):
                    continue
                subset.append(s[start:i+1])
                recur(i+1, subset)
                subset.pop()

        # 判断子串是否为回文串
        def helper(subStr):
            i, j = 0, len(subStr)-1
            while i <= j:
                if subStr[i] != subStr[j]:
                    return False
                i += 1
                j -= 1
            return True
    
        res = []
        recur(0, [])
        return res

if __name__ == '__main__':
    obj = Solution()
    print(obj.partition('aab'))
