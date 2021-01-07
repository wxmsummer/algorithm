class Solution:
    # 石头游戏 给一排石头堆，用一个数组nums表示，nums[i]表示第i堆有多少个石子
    # A和B轮流拿石子，每轮只能拿走最左边或最右边的一整堆石子，求所有石子被拿完后，先手和后手的最后得分之差
    def stoneGame(self, nums: list) -> int:
        length = len(nums)


    # first 表示先手 second 表示后手
    class Pair {
        int first, second
        Pair(int first, int second) {
            this.first = first
            this.second = second
        }
    }

    # dp[i][j]表示i到j的连续石头堆
    # dp[i][j].first表示对于i到j这部分石堆，先手能获得的最高分
    # dp[i][j].second表示对于i到j这部分石堆，后手能获得的最高分
    int stoneGame(int[] piles) {
        int n = piles.length
        Pair[][] dp = new Pair[n][n]
        # 初始化dp数组
        for(int i = 0; i < n; i++) {
            for(int j = i; j < n; j++) {
                dp[i][j] = new Pair(0, 0)
            }
        }
        # 填入base case，表示先手拿完，后手拿0分
        for(int i = 0; i < n; i++) {
            dp[i][i].first = piles[i]
            dp[i][i].second = 0
        }

        # 斜着遍历数组
        for (int l = 2; l <= n; l++){
            for (int i = 0; i <= n - l; i++) {
                int j = l + i - 1
                # 先手选择左边或右边的分数
                # 如果先手选择左边石堆，则接下来先手变为i+1到j的后手选择
                int left = piles[i] + dp[i+1][j].second
                # 如果先手选择右边石堆，则接下来先手变为i到j-1的后手选择
                int right = piles[j] + dp[i][j-1].second
                if(left < right) {
                    # 先手和后手是相对的，这次的先手变为下次的后手
                    dp[i][j].first = left
                    dp[i][j].second = dp[i+1][j].first
                } else {
                    dp[i][j].first = right
                    dp[i][j].second = dp[i][j-1].first
                }
            }
        }
        Pair res = dp[0][n-1]
        return res.first - res.second
    }

