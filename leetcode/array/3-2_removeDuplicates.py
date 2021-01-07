class Solution:
    def removeDuplicates(self, nums:list) -> int:
        j, count = 1, 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                count += 1
            else:
                count = 1
            if count <= 2:
                nums[j] = nums[i]
                j += 1
            print('nums:', nums)
        return j

if __name__ == '__main__':
    obj = Solution()
    print(obj.removeDuplicates([0,0,1,1,1,1,2,3,3]))