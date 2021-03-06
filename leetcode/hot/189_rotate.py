class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % len(nums)
        new_num = [0] * n
        for i in range(n):
            new_num[(i+k)%n] = nums[i]

        for i in range(n):
            nums[i] = new_num[i]
        