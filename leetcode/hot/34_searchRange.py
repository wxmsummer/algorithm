class Solution:
    def searchRange(self, nums:list, target:int) -> list:
        left = getRightBorder(nums, target - 1)
        right = getRightBorder(nums, target)
        if left == right :
            return [-1, -1]
        return [left, right - 1]
    
    # 获取大于等于target的第一个数
    def getRightBorder(self, nums:list, target:int) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if target >= nums[m]:
                i = m + 1
            else:
                j = m - 1
        return i