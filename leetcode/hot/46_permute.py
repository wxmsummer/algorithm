# 全排列

class Solution:
    def permute(self, nums: list) -> list:
        # 递归+回溯
        def backtrack(first):
            # 如果走完，则加入解集
            if first == n:
                res.append(list(nums))
            # 对每一个数，都逐个进行交换
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[i], nums[first] = nums[first], nums[i]

        n = len(nums)
        res = []
        backtrack(0)

        return res