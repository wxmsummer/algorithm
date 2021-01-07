class Solution:
    def maxProfit(self, prices:list) -> int:
        
        if prices = []:
            return 0
        dp = [0] * len(prices)
        min_ = prices[0]
        for i in range(len(prices)):
            # 需要维护一个最小值
            min_ = min (min_, prices[i])
            print('dp:', dp)
            dp[i] = max(dp[i-1], prices[i] - min_)
        
        return dp[i]

if __name__ == '__main__':
    obj = Solution()
    print(obj.maxProfit([7,1,5,3,6,4]))
    # print(obj.maxProfit([1,2,3,4,5]))
    # print(obj.maxProfit([7,6,4,3,1]))