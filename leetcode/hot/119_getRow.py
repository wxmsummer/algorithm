class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = []
        numRows = rowIndex + 1
        for i in range(1, numRows+1):
            tmp = [0] * i
            tmp[0] = 1
            tmp[-1] = 1
            res.append(tmp)
        
        for i in range(2, numRows):
            for j in range(1, i):
                res[i][j] = res[i-1][j-1] + res[i-1][j]

        return res[rowIndex]