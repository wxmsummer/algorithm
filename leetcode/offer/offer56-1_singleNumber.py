# 只出现一次的数字

class Solution:
    def singleNumbers(self, nums: List[int]) -> int:
        single_number = 0
        for num in nums:
            single_number ^= num
        return single_number
       