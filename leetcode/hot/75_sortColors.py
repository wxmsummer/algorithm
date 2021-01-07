from collections import defaultdict

class Solution:
    # 存储0，1，2个数，最后进行覆盖
    def sortColors(self, nums: list) -> None:
        dic = defaultdict(int)
        length = len(nums)
        for i in range(length):
            dic[nums[i]] += 1
        cur = 0
        for i in range(3):
            for j in range(dic[i]):
                nums[cur] = i
                cur += 1
        print('dic:', dic)
        return nums

    # 双哨兵法
    def sortColors(self, nums: list) -> None:
        length = len(nums)
        left_guard, right_guard = 0, length-1
        i = 0
        while i <= right_guard and left_guard < right_guard:
            # print('i, left, right:', i, left_guard, right_guard)
            if i < left_guard:
                i = left_guard
            elif nums[i] == 0:
                nums[i], nums[left_guard] = nums[left_guard], nums[i]
                left_guard += 1
            elif nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                nums[i], nums[right_guard] = nums[right_guard], nums[i]
                right_guard -= 1
            # print('nums:', nums)
            # i += 1
        return nums

if __name__ == '__main__':
    obj =Solution()
    print(obj.sortColors([2,0,2,1,1,0]))
    print(obj.sortColors([2,0,1]))
    print(obj.sortColors([0]))
