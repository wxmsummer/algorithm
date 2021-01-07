from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int: 
        nums = [float('-inf')] + nums + [float('-inf')]
        left, right = 0, len(nums) - 1
        while left < right:
            print('left:', left)
            print('right:', right)
            mid = (left + right) // 2
            print('mid:', mid)
            if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
                return mid - 1
            elif nums[mid-1] > nums[mid]:
                right = mid
            elif nums[mid] < nums[mid+1]:
                left = mid

if __name__ == '__main__':
    obj = Solution()
    # print(obj.findPeakElement([1]))
    print(obj.findPeakElement([1, 2]))
    # print(obj.findPeakElement([1,2,3,1]))
    # print(obj.findPeakElement([1,2,1,3,5,6,4]))