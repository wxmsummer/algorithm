# 调整数组顺序使奇数位于偶数前面

# 两次遍历
class Solution:
    def exchange(self, nums: list) -> list:
        newList = []
        for num in nums:
            if num % 2 == 1:
                newList.append(num)
        
        for num in nums:
            if num % 2 == 0:
                newList.append(num)
        return newList

# 原数组，直接交换，双指针
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1
        while i < j:
            while i < j and nums[i] & 1 == 1: i += 1
            while i < j and nums[j] & 1 == 0: j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        return nums


if __name__ == '__main__':
       obj = Solution()
       print(obj.exchange([1, 2, 3, 4]))