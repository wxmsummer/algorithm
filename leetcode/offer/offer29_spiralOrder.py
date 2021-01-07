# 顺时针打印矩阵

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        newList = []
        
        if not matrix:
            return newList
        i, j = 0, 0
        newList.append(matrix[0][0])
        # 如果走到右边界则往下，然后往左，往上，，依次循环
        # 每次走过，把走过的格子标记为走过，下次则不会再走
        while len(newList) < len(matrix) * len(matrix[0]):
            while j < len(matrix[0])-1 and matrix[i][j+1] != '':
                newList.append(matrix[i][j+1])
                matrix[i][j] = ''
                j += 1
            while i < len(matrix)-1 and matrix[i+1][j] != '':
                newList.append(matrix[i+1][j])
                matrix[i][j] = ''
                i += 1
            while j > 0 and matrix[i][j-1] != '':
                newList.append(matrix[i][j-1])
                matrix[i][j] = ''
                j -= 1
            while i > 0 and matrix[i-1][j] != '':
                newList.append(matrix[i-1][j])
                matrix[i][j] = ''
                i -= 1
        return newList