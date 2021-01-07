# 不同的二叉搜索树
# 设n个节点的二叉搜索树的个数为G(n)，f(i)为以i为根的二叉搜索树的个数
# 则有：G(n) = f(1) + f(2) + f(3)+ ... + f(n)
# 当以i为根节点时，其左子树节点个数为i-1个，右子树节点个数为n-i
# 则有：f(i) = G(i-1) * G(n-i)
# 综合以上两个公式可得 卡特兰数 公式
# G(n) = G(0) * G(n-1) + G(1) * G(n-2) + ... + G(n-1)*G(0)


class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1] * dp[i-j]
        return dp[n]
        