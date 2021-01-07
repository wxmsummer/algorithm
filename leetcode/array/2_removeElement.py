class Solution:
    def removeElement(self, nums:list, val:int) -> int:
        if not nums:
            return 0
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] == val and nums[j] != val:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            if nums[i] != val:
                i += 1
            if nums[j] == val:
                j -= 1
            print('nums:', nums)
        if nums[j] == val:
            return j
        else:
            return j+1

    def removeElement(self, nums, val):
        n, i, j = len(nums), -1, 0
        while j <= n-1:
            if nums[j] != val:
                i += 1
                nums[i] = nums[j]
            j += 1
        return i+1
        
if __name__ == '__main__':
    obj = Solution()
    print(obj.removeElement([0,1,2,2,3,0,4,2], 2))
    print(obj.removeElement([3,2,2,3], 2))
    print(obj.removeElement([1], 1))