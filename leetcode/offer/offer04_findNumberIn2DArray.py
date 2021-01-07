# 在二维数组查找

def findNumberIn2DArray(matrix: List[List[int]], target: int) -> bool:
    rows = len(matrix)
    if rows == 0:
        return False
    columns = len(matrix[0])
    if  columns == 0:
        return False

    row, column = 0, columns-1
    # 从右上角开始查找，如果小了，往下，如果大了，往左
    while(row < rows and column >= 0):
        num = matrix[row][column]
        if target == num:
            return True
        elif target > num:
            row += 1
        else:
            column -=  1
    return False
    
if __name__ == '__main__':
    print(findRepeatNumber())