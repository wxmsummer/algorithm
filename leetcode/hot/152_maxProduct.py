# 最大连续子数组乘积

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        res = nums[0]
        # max_p表示以nums[i]结尾的子数组的最大乘积
        # min_p表示以nums[i]结尾的子数组的最小乘积

        max_p = nums[0]
        min_p = nums[0]
        for i in range(1, n):
            # 最大的数乘以负数会变为最小的数
            # 最小的数乘以负数也可能变为最大的数
            temp = max_p
            max_p = max(max_p * nums[i], nums[i], min_p*nums[i])
            min_p = min(min_p * nums[i], nums[i], temp*nums[i])
            res = max(res, max_p)
            print('max_p:', max_p)
            print('min_p:', min_p)
            print('res:', res)
        return res

if __name__ == '__main__':
    obj = Solution()
    print(obj.maxProduct([2,3,-2,4]))
    print(obj.maxProduct([-4,-3,-2]))