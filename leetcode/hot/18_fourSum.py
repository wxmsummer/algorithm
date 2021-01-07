class Solution:
    # def fourSum(self, nums:list, target:int) -> list:
    #     length, res = len(nums), []
    #     nums.sort()
    #     for i in range(length):
    #         for j in range(i+1, length):
    #             for k in range(j+1, length):
    #                 for l in range(k+1, length):
    #                     if nums[i] + nums[j] + nums[k] + nums[l] == target:
    #                         res.append([nums[i],nums[j], nums[k], nums[l]])
    #     return res

if __name__ == '__main__':
    obj = Solution()
    print(obj.fourSum([1, 0, -1, 0, -2, 2], 0))