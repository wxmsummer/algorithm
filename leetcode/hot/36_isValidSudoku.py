class Solution:
    # 一次遍历 使用字典存储当前行是否重复
    # 使用字典数组存储当前列是否重复
    # 使用字典数组存储当前九宫格是否重复
    def isValidSudoku(self, board: list) -> bool:
        row_dic = {}
        box_dic = [{} for i in range(3)]
        col_dic = [{} for i in range(9)]
        row_len, col_len = len(board), len(board[0])
        for i in range(row_len):
            # 重置九宫格
            if i % 3 == 0:
                box_dic = [{} for i in range(3)]
            for j in range(col_len):
                cur = board[i][j]
                # 如果不是'.'，才进行判断
                if cur != '.':
                    # 判断行
                    if cur in row_dic:
                        return False
                    row_dic[cur] = 1
                    # 判断列
                    if cur in col_dic[j]:
                        return False
                    col_dic[j][cur] = 1
                    
                    # 判断九宫格
                    box_idx = j // 3
                    if cur in box_dic[box_idx]:
                        return False
                    box_dic[box_idx][cur] = 1
                
                # 每一行，重置行字典
                if j == col_len - 1:
                    row_dic = {}

                # print('row:', row_dic)
                # print('col:', col_dic)
                # print('box_dic:', box_dic)

        return True

if __name__ == '__main__':
    obj = Solution()
    # print(obj.isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))
    print(obj.isValidSudoku([[".",".","4",".",".",".","6","3","."],[".",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".","9","."],[".",".",".","5","6",".",".",".","."],["4",".","3",".",".",".",".",".","1"],[".",".",".","7",".",".",".",".","."],[".",".",".","5",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]))
