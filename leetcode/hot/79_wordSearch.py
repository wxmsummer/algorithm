# 单词搜索

class Solution:
    # 回溯法
    def exist(self, board: list, word: str) -> bool:
        length = len(word)
        # i,j是board当前坐标，idx是word当前索引
        def dfs(i, j, idx) -> bool:
            # 如果idx等于length，说明已经完全匹配，返回True
            if idx == length:
                return True
            # 如果越界，返回False
            if i < 0 or i >= row_len or j < 0 or j >= col_len:
                return False
            # 记录tmp，用于回溯
            tmp = board[i][j]
            # 如果已走过，或者不等，返回False
            if tmp == '#' or tmp != word[idx]:
                return False
            print('board:', board)
            print('idx:', word[idx])
            # 如果某处相等
            if word[idx] == tmp:
                # 设置已走
                board[i][j] = '#'
                # 往上下左右走
                if dfs(i+1, j, idx+1) or dfs(i-1, j, idx+1) or dfs(i, j+1, idx+1) or dfs(i, j-1, idx+1):
                    return True
                # 错了就回溯
                else:
                    board[i][j] = tmp

        row_len, col_len = len(board), len(board[0])
        # 需要以每个位置开始搜索
        for i in range(row_len):
            for j in range(col_len):
                if dfs(i, j, 0):
                    return True
        # 如果所有的都检索完了，还是没有True，说明不存在
        return False
        

if __name__ == '__main__':
    obj = Solution()
    # print(obj.exist([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], 'FCE'))
    print(obj.exist([["C","A","A"],["A","A","A"],["B","C","D"]], 'AAB'))
    # print(obj.exist([['A']], 'A'))