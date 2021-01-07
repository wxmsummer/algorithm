class Solution:
    def removeDuplicates(self, nums:list) -> int:
        i, j = 0, 0
        while j < len(nums):
            print('j:', j)
            if j+1 < len(nums) and nums[j+1] == nums[j]:
                j += 1
            else:
                nums[i] = nums[j]
                i += 1
                j += 1
            print('nums:', nums)
        return i

if __name__ == '__main__':
    obj = Solution()
    print(obj.removeDuplicates([0]))