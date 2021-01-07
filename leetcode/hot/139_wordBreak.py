class Solution:
    # 记忆化递归
    # @functools.lru_cache(None) 禁止开启lru缓存机制
    def wordBreak(self, s: str, wordDict: list) -> bool:
        import functools
        @functools.lru_cache(None)
        def backTrack(s):
            if not s:
                return True
            res = False
            for i in range(1, len(s)+1):
                if s[:i] in wordDict:
                    res = backTrack(s[i:]) or res
            return res

        return backTrack(s)

    # 动态规划
    # dp[i]表示以i结尾的字串是否已经匹配
    # s[i:j]表示以i开头，以j结尾的字串
    def wordBreak(self, s: str, wordDict: list) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        for i in range(n):
            for j in range(i+1, n+1):
                if dp[i] and (s[i:j] in wordDict):
                    dp[j] = True
        return dp[-1]

if __name__ == '__main__':
    obj = Solution()
    print(obj.wordBreak(s = "leetcode", wordDict = ["leet", "code"]))