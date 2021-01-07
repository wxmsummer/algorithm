class Solution:
    def spiralOrder(self, matrix: list) -> list:
        row_len, col_len = len(matrix), len(matrix[0])
        res = []
        i,j = 0, 0
        while len(res) < row_len * col_len - 1:
            while 0 <= j+1 < col_len and matrix[i][j+1] != '/':
                res.append(matrix[i][j])
                matrix[i][j] = '/'
                j += 1

            while 0 <= i+1 < row_len and matrix[i+1][j] != '/':
                res.append(matrix[i][j])
                matrix[i][j] = '/'
                i += 1

            while 0 <= j-1 < col_len and matrix[i][j-1] != '/':
                res.append(matrix[i][j])
                matrix[i][j] = '/'
                j -= 1

            while 0 <= i-1 < row_len and matrix[i-1][j] != '/':
                res.append(matrix[i][j])
                matrix[i][j] = '/'
                i -= 1

        # 遍历到最后，剩一个中心节点，将其加入res   
        res.append(matrix[i][j])
        return res

if __name__ == '__main__':
    obj = Solution()
    print(obj.spiralOrder([[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]]))