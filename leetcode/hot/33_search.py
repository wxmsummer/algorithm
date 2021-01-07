

class Solution:
    # 二分搜索
    def search(self, nums:list, target:int) -> int:
        i, j = 0, len(nums)-1
        while i <= j:
            m = (i+j) // 2
            # 若发现tagrget则返回下标
            if nums[m] == target:
                return m
            # 如果左半边有序，且tar在左半边，则继续在左半边搜索
            if nums[0] <= nums[m]:
                if nums[0] <= target < nums[m]:
                    j = m - 1
                else:
                    i = m + 1
            # 如果右半边有序，且tar在右半边，则继续在右半边搜索
            else:
                if nums[m] < target <= nums[j]:
                    i = m + 1
                else:
                    j = m - 1

        # 找不到target则返回-1 若nums为空，则i=0 > j=-1，也返回-1
        return -1