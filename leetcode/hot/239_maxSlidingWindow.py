# 滑动窗口最大值

from typing import List

class Solution:
    # 使用单调队列
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = collections.deque()
        # 先初始化队列
        # 队列q中存储的是元素下标
        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
        
        ans = [nums[q[0]]]
        for i in range(k, n):
            # 当队尾元素小于当前元素时，将队尾元素出队
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            # 如果发现队首下标已经走出窗口，则将其移出队列
            while q[0] <= i - k:
                q.popleft()
            ans.append(nums[q[0]])

        return ans
