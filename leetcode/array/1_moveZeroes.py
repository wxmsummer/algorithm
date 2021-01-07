class Solution:
    # def moveZeroes(self, nums:list) -> list:
    #     count = 0
    #     for i in range(len(nums)-1, -1, -1):
    #         if nums[i] == 0:
    #             count += 1
    #             for j in range(i, len(nums)-count):
    #                 nums[j], nums[j+1] = nums[j+1], nums[j]
    #                 print('nums:', nums)
    #     return nums

    # 双指针，遇到不为0的就和0交换
    def moveZeroes(self, nums:list) -> list:
        if not nums:
            return 0
        j = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
            print('nums:', nums)
        return nums

if __name__ == '__main__':
    obj = Solution()
    print(obj.moveZeroes([0, 1, 2, 0, 12]))