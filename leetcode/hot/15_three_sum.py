class Solution:
    # 解法1 三层循环暴力遍历，O(n^3)
    # def threeSum(self, nums: list, target: int) -> list:
    #     res, length = [], len(nums)
    #     nums.sort()
    #     for i in range(length-2):
    #         for j in range(i+1, length-1):
    #             for k in range(j+1, length):
    #                 if nums[i] + nums[j] + nums[k] == target:
    #                     res.append([nums[i], nums[j], nums[k]])
    #                 print(res)
    #     return res

    # 解法2 使用dic，保存两数，由第三数匹配，降低时间复杂度，O(n^2)
    # def threeSum(self, nums: list, target: int) -> list:


    # 解法3 排序后，对每一个数，使用双指针，时间复杂度，O(n^2)
    def threeSum(self, nums: list, target: int) -> list:
        length = len(nums)
        nums.sort()
        ans = list()

        for i in range(length):
            # 相同的元素直接走过去，只用一个
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # 右指针
            right = length - 1
            # 用于判断是否构成解
            tmp = target - nums[i]
            # 左指针开始往右走
            for left in range(i+1, length):
                # 左指针遇到相同的元素也直接走过去，只用一个
                if left > i+1 and nums[left] == nums[left-1]:
                    continue
                # 右指针不断往左移动，然后判断是否过大
                while right > left and nums[left] + nums[right] > tmp:
                    right -= 1
                    # 如果发现解，将其加入解答
                if left == right:
                    break
                if nums[left] + nums[right] == tmp:
                    ans.append([nums[i], nums[left], nums[right]])
        return ans

if __name__ == '__main__':
    obj = Solution()
    # print(obj.threeSum([-1, 0, 1, 2, -1, -4], 0))
    print(obj.threeSum([1, -1, -1, 0], 0))