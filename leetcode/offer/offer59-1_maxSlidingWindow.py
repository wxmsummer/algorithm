# 滑动窗口的最大值

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left, right = 1-k, 0
        ans, queue = [], []
        while right < len(nums):
            queue.append(nums[right])
            # 删除小数，留下大数。len(queue) >= 2 为了确保 queue[-2] 不越界
            while len(queue) >= 2 and queue[-2] < queue[-1]:
                queue.pop(-2)
            # 左窗口移动，并将队列中的最大数加入解答
            if left >= 0:
                ans.append(queue[0])
            # 移出窗口的数等于队首，则对应从队列中删除
            if queue[0] == nums[left]:
                queue.pop(0)
            
            right += 1
            left += 1
        
        return ans