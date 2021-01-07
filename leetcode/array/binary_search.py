
class Solution:
    def binary_search(self, nums:list, target:int):
        i, j = 0, len(nums)
        while i < j:
            m = (i + j) // 2
            if nums[m] >= target:
                j = m
            else:
                i = m + 1
        if i == len(nums):
            return -1
        return i

if __name__ == '__main__':
    obj = Solution()
    print(obj.binary_search([2,3,3,3,3,3], 3) )


# DPRC开发
# 讲项目，提高
# 细节，对项目的深入度
# go相关
# 比较深入的点，通信协议，分布式系统，稳定性，可拓展性
# 代码，逻辑需要更清晰，思路
# 知识储备，能力体现
