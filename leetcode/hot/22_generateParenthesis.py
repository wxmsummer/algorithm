class Solution():
    def generateParenthesis(self, n:int) -> list:
        res, tmp = [], []
        # left_num 表示还能放多少个左括号, right_num 表示还能放多少右括号
        def backtrack(left_num, right_num):
            # 如果左括号和右括号都放完了，说明这一轮回溯完成，将结果加入结果集
            if left_num == 0 and right_num == 0:
                res.append(''.join(tmp))
            # 左括号可以随意放，只要数量大于0
            if left_num > 0:
                tmp.append('(')
                # 放了左括号之后，回溯，左括号可放数量减一
                backtrack(left_num-1, right_num)
                # 回溯后恢复上一状态
                tmp.pop()
            # 右括号可放的数量必须大于左括号可放的数量，即必须先放了左括号才能放右括号
            if left_num < right_num:
                tmp.append(')')
                # 回溯，右括号可放数量减一
                backtrack(left_num, right_num-1)
                # 恢复回溯前状态
                tmp.pop()

        backtrack(n, n)

        return res

if __name__ == '__main__':
    obj = Solution()
    print(obj.generateParenthesis(0))