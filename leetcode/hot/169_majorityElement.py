from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            if count == 0:
                votes = nums[i]
                count += 1
                continue
            if nums[i] == votes:
                count += 1
            else:
                count -= 1
        return votes

if __name__ == '__main__':
    obj = Solution()
    print(obj.majorityElement([3,3,4]))
    # print(obj.majorityElement([2,2,1,1,1,2,2]))