class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        length = len(nums)
        nums.sort()
        res = list()
        for i in range(len(nums)):
            j = length - 1
            tmp = target - nums[i]
            while j > i:
                if nums[j] == tmp:
                    res.append([nums[i], nums[j]])
                    break
                j -= 1
        return res

    # 使用dic保存
    def twoSum(self, nums: list, target: int) -> list:
        dic = {}
        # 字典的键是nums[i]，值是下标
        # 遍历的时候，查询target - num 是否在字典的key中
        for i in range(len(nums)):
            num = nums[i]
            # in 是在字典中查找 是否存在该键
            # 如果该键存在，则与当前数构成一对，则把下标返回
            expect = target - num
            if expect in dic:
                return [dic[expect], i]
            dic[nums[i]] = i
        return []

if __name__ == '__main__':
    obj = Solution()
    print(obj.twoSum([2, 3, 6, 7, 11, 15], 9))