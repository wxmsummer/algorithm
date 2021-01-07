# 搜索旋转排序数组

class Solution:
    # 思路一，直接遍历解决
    def search(self, nums: list, target: int) -> bool:
        length = len(nums)
        for i in range(length):
            if nums[i] == target:
                return True
        return False

    # 思路二，二分法解决
    # 数组从任意位置分隔开，至少有一半是有序的
    # 先找到哪一段是有序的(根据这一段的端点确定)，然后看target在不在这一段里
    # 如果在，就在这一段里找，否则就在另一段里找
    def search(self, nums: list, target: int) -> bool:
        l, r = 0, len(nums)-1
        while l <= r:
            print('l,r:', l, r)
            mid = (l+r) // 2
            if nums[mid] == target:
                return True
            # 如果左半边有序
            elif nums[mid] > nums[l]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # 如果右半边有序
            elif nums[mid] < nums[l]:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            # 如果不能确定
            elif nums[mid] == nums[l]:
                l += 1
        return False

if __name__ == '__main__':
    obj = Solution()
    print(obj.search([2,5,6,0,0,1,2], 3))