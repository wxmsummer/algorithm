class Solution:
    def nextPermutation(self, nums: list):
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums == []:
            return
        length = len(nums)
        flag1, flag2 = -1, 0
        for i in range(length-1, 0, -1):
            if nums[i-1] < nums[i]:
                flag1 = i-1
                break
        print('flag1:', flag1)
        for j in range(length-1, 0, -1):
            if nums[j] > nums[flag1]:
                flag2 = j
                break
        print('flag2:', flag2)
        if flag1 != -1:
            nums[flag1], nums[flag2] = nums[flag2], nums[flag1]

        left, right = flag1+1, length-1
        print('left:', left, 'right:', right)
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        
        return nums

if __name__ == '__main__':
    obj = Solution()
    # print(obj.nextPermutation([1, 5, 3, 2, 4]))
    print(obj.nextPermutation([1, 2]))
    print(obj.nextPermutation([5, 4, 3, 2, 1]))