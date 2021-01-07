class Solution:
    def nums_pair(self, nums, k):
        count = 0
        nums.sort()
        i, j = 0, len(nums) - 1
        print('nums:', nums)
        # 1， 2， 3， 4， 5， 7
        while i < j:
            s = nums[i] + nums[j]
            if s > k:
                j -= 1
            elif s < k:
                i += 1
            else:
                count += 1
                j -= 1
        return count


# class Solution:
#     def nums_pair(self, nums: list, target: int) -> list:
#         dic = dict()
#         count = 0
#         for i, num in enumerate(nums):
#             # 检查和是否等于target
#             if target - num in dic:
#                 count += 1
#             # 记录下标
#             dic[nums[i]] = i
#         return count


if __name__ == '__main__':
    obj = Solution()
    print(obj.nums_pair([2, 3, 4, 7, 1, 5, 6, -1, 8, 3.5, 3.5], 7))