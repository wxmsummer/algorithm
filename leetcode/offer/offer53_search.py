class Solution:
    def search(self, nums: list, target: int) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] == target:
                while i <len(nums) and nums[i] == target:
                    count += 1
                    i += 1
                return count
        return 0

# 二分法求解，分别找到左边界和右边界
class Solution:
    def search(self, nums: list, target: int) -> int:
        def helper(tar):
            i, j = 0, len(nums) - 1
            while i <= j:
                m = (i + j) // 2
                if nums[m] <= tar:
                    i = m + 1
                else:
                    j = m - 1
            return i
        return helper(target) - helper(target-1)

if __name__ == '__main__':
    obj = Solution()
    print(obj.search([5,7,7,8,8,10], 7))