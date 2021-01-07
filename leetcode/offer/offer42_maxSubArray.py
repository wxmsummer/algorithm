# 连续子数组的最大和

class Solution():
    # 动态规划，设dp[i]代表以元素nums[i]为结尾的连续子数组最大和
    # 若dp[i-1] <= 0，说明dp[i-1]+nums[i] <= nums[i]
    # 转移方程：当dp[i-1]>0时，dp[i] = dp[i-1] + nums[i]
    # 否则，dp[i] = nums[i]
    # 此处可直接将nums作为dp数组

    def maxSubArray(self, nums) -> int:
        for i in range(1, len(nums)):
            nums[i] += max(nums[i-1], 0)
        print(nums)
        return max(nums)


if __name__ == '__main__':
    
    obj = Solution()
    print(obj.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))