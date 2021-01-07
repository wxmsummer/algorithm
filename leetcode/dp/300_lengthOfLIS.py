# 最长上升子序列

class Solution:
    # 动态规划
    # dp[i]表示以nums[i]结尾的最长上升子序列的长度
    def lengthOfLIS(self, nums:list) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            # 状态转移方程：寻找比nums[i]小的数nums[j]，并取dp[j]中最大的并加1
            # 从nums[0] 找到 nums[i-1]
            for j in range(0, i):
                # 如果nums[j] < nums[i]
                if nums[j] < nums[i]:
                    # 修改dp[i]的值，为符合条件的dp的最大值
                    dp[i] = max(dp[i], dp[j] + 1)
                print('dp:', dp)
        res = 0
        # 寻找最大的dp[i]
        for i in range(len(nums)):
            res = max(res, dp[i])
        return res

if __name__ == '__main__':
    obj = Solution()
    print(obj.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
