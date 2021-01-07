class Solution:
    def generateMatrix(self, n: int) -> list:
        row_len, col_len = n, n
        res = []
        i,j = 0, 0
        matrix = [[0 for i in range(n)] for i in range(n)]
        num = 1
        while num < row_len * col_len:
            while 0 <= j+1 < col_len and matrix[i][j+1] == 0:
                matrix[i][j] = num
                j += 1
                num += 1

            while 0 <= i+1 < row_len and matrix[i+1][j] == 0:
                matrix[i][j] = num
                i += 1
                num += 1

            while 0 <= j-1 < col_len and matrix[i][j-1] == 0:
                matrix[i][j] = num
                j -= 1
                num += 1

            while 0 <= i-1 < row_len and matrix[i-1][j] == 0:
                matrix[i][j] = num
                i -= 1
                num += 1

        print('i,j:', i,j)
        # 遍历到最后，剩一个中心节点，将其加入res   
        matrix[i][j] = num
        return matrix
        print('matrix:', matrix)

if __name__ == '__main__':
    obj = Solution()
    print(obj.generateMatrix(4))