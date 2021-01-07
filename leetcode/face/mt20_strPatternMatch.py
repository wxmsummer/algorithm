# def strPartternMatch():
#     a = input()
#     b = input()
#     i, j = len(a)-1, len(b)-1
#     while i > -1:
#         if i == 0 and a[0] == '*':
#             print(1)
#             return
#         print('i:',i,'a:', a[:i+1], 'b:', b[:j+1])    
#         if j > 0 and a[i] == b[j] or a[i] == '?':
#             i -= 1
#             j -= 1
#             continue
#         elif a[i] == '*':
#             if i > 0 and a[i-1] == '*':
#                 i -= 1
#                 continue
#             if j > 0 and a[i-1] == b[j] or a[i-1] == '?':
#                 a = a[:i-1] + a[i]
#                 i -= 1
#             j -= 1
#             continue
#         else:
#             print(0)
#             return 
#     print(1)
#     return  

def strPartternMatch():
    # a为模式串
    a = input()
    # b为主串
    b = input()
    # 
    m, n = len(a), len(b)
    # dp[i][j] 表示模式串的前i位字符是否能和主串的前j位字符匹配
    # dp有m行，n列
    dp = [[0] * (n+1) for i in range(m+1)]
    # 初始化：空串和空串匹配
    dp[0][0] = 1

    # 初始化：模式串若全为*，也匹配,j=0说明主串为空
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] and a[i-1] == '*'

    for i in range(1, m+1):
        for j in range(1, n+1):
            print('dp:', dp)
            # 如果模式串的第i个字符和主串的第j个字符相等，或者模式串的第i个字符为?
            # 则模式串前i位字符和主串前j位字符是否匹配 取决于 模式串前i-1位字符和主串前j-1位字符是否匹配
            if a[i-1] == b[j-1] or a[i-1] == '?':
                dp[i][j] = dp[i-1][j-1]
            # 如果模式串的第i个字符为'*'，则模式串前i位字符和主串前j位字符是否匹配 取决于 
            # 模式串前i-1位字符和主串前j位字符是否匹配（即模式串删掉*再进行匹配） 或者 模式串前i位字符和主串前j-1位字符是否匹配（即主串删掉一个字符）
            if a[i-1] == '*':
                dp[i][j] = dp[i-1][j] or dp[i][j-1]

    return dp[m][n]

if __name__ == '__main__':
    print(strPartternMatch())