from typing import List

class Solution:
    # 双指针
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        ans = n + 1
        i, j = 0, 0
        temp_sum = 0
        while j < n:
            temp_sum += nums[j]
            while temp_sum >= s:
                ans = min(ans, j-i+1)
                temp_sum -= nums[i]
                i += 1
            j += 1
        if ans == n+1:
            return 0
        else:
            return ans

if __name__ == '__main__':
    obj = Solution()
    print(obj.minSubArrayLen(7, [2,3,1,2,4,3]))
    print(obj.minSubArrayLen(4, [1,4,4]))