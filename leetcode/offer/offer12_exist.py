# 矩阵中的路径
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 深度优先搜索 + 回溯 + 剪枝
        # (i, j) 代表当前位置，k代表字符串当前字符
        def dfs(i, j, k):
            # 如果超出矩阵边界，返回false
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]):
                return False
            # 如果当前字符不匹配，直接返回false
            if board[i][j] != word[k]:
                return False
            # 说明匹配完成
            if k == len(word) - 1:
                return True
            # 先记录当前字符，方便恢复
            temp = board[i][j]
            # 标记，代表已走过
            board[i][j] = "/"

            # 往上下左右回溯
            res = dfs(i+1, j, k+1) or dfs(i-1, j, k+1) or dfs(i, j+1, k+1) or dfs(i, j-1, k+1)
            # 恢复原字符
            board[i][j] = temp
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                # 对每一个起始点，都要走一次
                if dfs(i, j, 0):
                    return True
        return False

if __name__ == '__main__':

    obj = Solution()
    print(obj.exist())