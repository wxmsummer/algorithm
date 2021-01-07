# 搜索二维矩阵

class Solution:
    def searchMatrix(self, matrix: list, target: int) -> bool:
        if matrix == []:
            return False
        row_len, col_len = len(matrix), len(matrix[0])
        i, j = 0, col_len-1
        # 从右上角开始搜索，如果小于target就往下搜索，大于target就往左搜索
        while i < row_len and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1
        
        return False