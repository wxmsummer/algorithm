# 分割数组为连续子序列

from typing import List
from collections import defaultdict


class Solution:
    # 贪心算法，从后往前找
    def isPossible(self, nums: List[int]) -> bool:
        length = len(nums)
        dic = defaultdict(int)
        max_ = max(nums)
        for i in range(length):
            dic[nums[i]] += 1
        end = nums[-1]
        while True:
            start = end
            while start > 0 and dic[start-1] >= dic[start]:
                start -= 1
            if end - start + 1 < 3:
                print('start,end:', start, end)
                return False
            else:
                while start <= end:
                    dic[start] -= 1
                    if not dic[start]:
                        end = start - 1
                        break
                    start += 1
            if end == nums[0] - 1:
                return True
            else:
                while end and not dic[end]:
                    end -= 1

if __name__ == '__main__':
    obj = Solution()
    print(obj.isPossible([1,2,3,3,4,4,5,5]))
    print(obj.isPossible([1,2,3,3,4,5]))
    print(obj.isPossible([1,2,3,4,4,5]))
    print(obj.isPossible([1,2,3,3,4,4,5,5,6,6,7,8]))
    print(obj.isPossible([4,5,6,7,7,8,8,9,10,11]))