# 198 打家劫舍

from typing import List

# 动态规划问题
# 如果只有一间房屋 那么偷窃该房屋
# 如果有两间房屋 那么选择其中金额较大的房屋进行偷窃
# 如果大于2间房屋 那么，对于第k间房屋，有两个选项
# 1.如果偷窃第k间房屋，那么就不能偷窃第k-1间房屋，
# 此时偷窃总金额为前k-2间房屋的最高偷窃总金额与第k间房屋的金额之和
# 2.如果不偷窃第k间房屋，那么总金额与前k-1间房屋最高总金额相同
# 在两个选项中选择较大的一项，该项即前k间房屋能够偷窃到的最高总金额

# 设dp[i]表示前i间房屋能偷窃到的最高总金额
# 状态转移方程：dp[i] = max(dp[i-2]+nums[i], dp[i-1])
# 边界条件：
# dp[0] = nums[0]
# dp[1] = max(nums[0], nums[1])


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        length = len(nums)
        if length == 1:
            return nums[0]
        
        dp = [0] * length
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, length):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        
        return dp[length-1]