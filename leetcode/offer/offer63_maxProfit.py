class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        max_ = min_ = prices[0]
        res = 0

        for num in prices:
            # 如果发现了比min_更小的数，就更新min_，然后重置max_为0
            if num < min_:
                max_ = 0
                min_ = num
                continue
            # 如果发现了比max_更大的数，就更新max_，同时更新最大收益
            if num > max_:
                max_ = num
                res = max(res, max_ - min_)
        
        return res