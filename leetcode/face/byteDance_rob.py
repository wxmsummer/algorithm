
class Solution:
    def money(self, num_list) -> int:
        dp = [[0 for i in range(len(num_list))] for i in range(len(num_list))]
        # 二维数组，第一个数表示num_list下标，第二个数取值为0或1，表示取或不取该数
        dp[0][0] = 0
        dp[0][1] = 0
        for i in range(0, len(num_list)):
            # 
            dp[i][1] = dp[i-1][0] + num_list[i]
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])
            print(dp)
        return max(dp[len(num_list)-1][0], dp[len(num_list)-1][1])

if __name__ == '__main__':
    obj = Solution()
    print(obj.money([10,1,6,100,90,2]))