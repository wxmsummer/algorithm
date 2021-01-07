from typing import List
from collections import deque

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        
        def pick_max(nums, k):
            stack = []
            drop = len(nums) - k
            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:k]
        
        def merge(A, B):
            ans = []
            while A or B:
                bigger = A if A > B else B
                ans.append(bigger.pop(0))
            res = int(''.join(str(item) for item in ans))
            return res

        max_ = 0
        for i in range(k+1):
            if i <= len(nums1) and k - i <= len(nums2):
                A, B = pick_max(nums1, i), pick_max(nums2, k-i)
                max_ = max(max_, merge(A, B))
        return [int(x) for x in str(max_)]
        
if __name__ == '__main__':
    obj = Solution()
    print(obj.maxNumber(nums1 = [3, 4, 6, 5], nums2 = [9, 1, 2, 5, 8, 3], k=5))
