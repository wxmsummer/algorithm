# 正则匹配
class Solution:
    # 动态规划，需要从后往前推
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        
        f = [[False for i in range(m+1)] for i in range(n+1)]

        for i in  range(n+1):
            for j in range(m+1):
                if j == 0 :
                    f[i][j] = (i == 0)
                else:
                    # 如果p的最后一个字符不为 * ，则看s[i-1] 是否== p[j-1] 或 p[j-1] 是否== '.'
                    if p[j-1] != '*':
                        if (i > 0 and s[i-1] == p[j-1]) or (i > 0 and  p[j-1] == '.'):
                            f[i][j] = f[i-1][j-1]
                    # 如果p的最后一个字符为 *
                    else:
                        # 直接废掉p最后两个字符
                        if j >= 2:
                            f[i][j] |= f[i][j-2]
                        # s最后一个字符和p倒数第二个字符相等，或p倒数第二个字符为 . 则去掉s最后一个字符
                        if (i >= 1 and j >= 2 and s[i-1] == p[j-2]) or p[j-2] == '.':
                            f[i][j] |= f[i-1][j]
        return f[n][m]

if __name__ == '__main__':
       obj = Solution()
       print(obj.isMatch('', '.'))