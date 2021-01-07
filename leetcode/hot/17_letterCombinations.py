class Solution:
    def letterCombinations(self, digits: str) -> list:
        s, res = [], []
        dic = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        if digits == '':
            return []
        # 回溯算法，回溯参数为下标，用于推进
        def backtrack(index:int):
            # 回溯结束标志：将单次的结果加入到结果集中
            if index == len(digits):
                res.append(''.join(s))
            # 回溯中，
            else:
                digit = digits[index]
                for letter in dic[digit]:
                    # 当前该做的事
                    s.append(letter)
                    # 开启下一次回溯
                    backtrack(index + 1)
                    # 回溯结束，要恢复上一个状态，便于继续回溯
                    s.pop()
        # 从初始态开始进行回溯
        backtrack(0)
        return res
    
if __name__ == '__main__':
    obj = Solution()
    print(obj.letterCombinations('23'))
