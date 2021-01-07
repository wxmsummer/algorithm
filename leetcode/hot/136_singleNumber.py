class Solution:
    def singleNumber(self, nums: list) -> int:
        length = len(nums)
        res = nums[0]
        for i in range(1, length):
            res ^= nums[i]
            
        return res

