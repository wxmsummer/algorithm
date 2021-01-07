class Solution:
    # 递归回溯
    def combinationSum(self, candidates:list, target:int) -> list:
        # ans为解答集，combine为当前已组合，idx为当前位置
        def dfs(target, ans, combine, idx):
            # print('combine:', combine)
            # print('ans:', ans)
            # 如果当前位置已走完 return
            if idx == len(candidates):
                return
            # 发现解，加入解集
            if target == 0:
                ans.append(list(combine))
                return
            # 当前元素不取，往下走
            dfs(target, ans, combine, idx+1)
            # 如果tar减当前数大于等于0，继续尝试在此位置
            # 注意等于号必须取
            if target - candidates[idx] >= 0:
                combine.append(candidates[idx])
                # 继续往下走
                dfs(target - candidates[idx], ans, combine, idx)
                # 回溯
                combine.pop()
        ans = []
        dfs(target, ans, [], 0)
        return ans

if __name__ == '__main__':
    obj = Solution()
    print(obj.combinationSum([2, 3, 6, 7], 7))