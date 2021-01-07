class Solution:
    def rotate(self, matrix: list) -> None:
        row_len, col_len = len(matrix), len(matrix[0])
        for i in range(1, row_len):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(row_len):
            left, right = 0, col_len-1
            while left < right:
                matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
                left += 1
                right -= 1

        print('matrix:', matrix)

