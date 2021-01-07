# 三角形的最大周长

class Solution:
    def largestPerimeter(self, nums: list) -> int:
        if len(nums) < 3:
            return 0
        nums.sort()
        length = len(nums)
        i, j, k = length-3, length-2, length-1
        while i >= 0:
            if nums[i] + nums[j] > nums[k]:
                return nums[i] + nums[j] + nums[k]
            else:
                i -= 1
                j -= 1
                k -= 1
            if i < 0:
                return 0
        
        return 0

if __name__ == '__main__':
    obj = Solution()
    print(obj.largestPerimeter([1,1]))
    print(obj.largestPerimeter([2,1,2]))
    print(obj.largestPerimeter([1,2,1]))
    print(obj.largestPerimeter([3,2,3,4]))
    print(obj.largestPerimeter([3,6,2,3]))