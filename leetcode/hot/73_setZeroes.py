# 矩阵置零

class Solution:
    def setZeroes(self, matrix: list) -> None:
        row_len, col_len = len(matrix), len(matrix[0])

        # 使用额外的两个行数组和列数组来存储行和列中的零信息
        row_list = [1] * row_len
        col_list = [1] * col_len
        for i in range(row_len):
            for j in range(col_len):
                if matrix[i][j] == 0:
                    row_list[i] = 0
                    col_list[j] = 0
        
        # 记录好零的数量之后，遍历置零
        for i in range(row_len):
            if row_list[i] == 0:
                for j in range(col_len):
                    matrix[i][j] = 0
        
        for j in range(col_len):
            if col_list[j] == 0:
                for i in range(row_len):
                    matrix[i][j] = 0
                    
