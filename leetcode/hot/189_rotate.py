class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        for i in range(k):
            pre = nums[-1]
            for j in range(len(nums)):
                temp = nums[j]
                nums[j] = pre
                pre = temp
                print('nums:', nums)