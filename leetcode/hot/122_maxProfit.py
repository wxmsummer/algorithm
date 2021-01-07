class Solution:
    def maxProfit(self, prices:list) -> int:
        
        dp = [0] * len(prices)
        for i in range(len(prices)):
            print('dp:', dp)
            if i > 0 and prices[i] > prices[i-1]:
                # dp[i] 加上 prices[i] 减去上一次买入的价格
                dp[i] += dp[i-1] + prices[i] - prices[i-1] 
            else:
                dp[i] = dp[i-1]
        
        return dp[i]

if __name__ == '__main__':
    obj = Solution()
    print(obj.maxProfit([7, 1, 5, 3, 6, 4]))
    print(obj.maxProfit([1,2,3,4,5]))
    print(obj.maxProfit([7,6,4,3,1]))