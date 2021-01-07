class Solution:
    # 递归回溯
    def combinationSum2(self, candidates:list, target:int) -> list:
        # target为当前剩余目标值，combine为已加入的元素，begin为当前位置
        def dfs(target, combine, begin):
            # print('combine:', combine)
            # print('ans:')
            
            if target == 0:
                ans.append(list(combine))
                return
            
            # 从当前位置开始进行递归调用
            for i in range(begin, length):
                # 剪枝
                if candidates[i] > target:
                    return
                # 如果有相同元素，则只考虑其中一个
                if i > begin and candidates[i - 1] == candidates[i]:
                    continue
                
                combine.append(candidates[i])
                # 开启下一层递归
                dfs(i+1, combine, target - candidates[i])
                # 回溯
                combine.pop()
        length = len(candidates)
        if length == 0:
            return []
        candidates.sort()
        ans = []
        dfs(target, [], 0)
        return ans

if __name__ == '__main__':
    obj = Solution()
    print(obj.combinationSum2([2, 3, 6, 7], 7))