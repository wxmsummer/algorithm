# 旋转排序数组中的最小值

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        min_ = min(nums[0], nums[right])
        while left < right:
            mid = (left + right) // 2
            # 如果mid值大于left，那么left到mid这一段是有序的
            # 取最小值为 min(min_, nums[left])，然后在mid+1到right这一段继续查找
            if nums[mid] > nums[left]:
                left = mid+1
                min_ = min(min_, nums[left])
            # 如果mid值小于left，则mid到right这一段是有序的
            # 取最小值为 min(min_, nums[mid])，然后在left到mid这一段继续查找
            else:
                right = mid
                min_ = min(min_, nums[mid])
        return min_

if __name__ == '__main__':
    obj = Solution()
    print(obj.findMin([2,3,4,5,6,7,0]))
    print(obj.findMin([4,5,6,7,0,1,2]))
    print(obj.findMin([3,4,5,1,2]))
    print(obj.findMin([2,1]))
    print(obj.findMin([5,1,2,3,4]))
