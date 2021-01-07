# 和为s的连续正数序列

class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        i, j, sum, res = 1, 1, 0, []
        while i <= target // 2:
            if sum < target:
                sum += j
                j += 1
            elif sum > target:
                sum -= i
                i += 1
            else:
                res.append(list(range(i, j)))
                sum -= i
                i += 1
        return res