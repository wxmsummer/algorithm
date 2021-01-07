class Solution:
    def generate(self, numRows: int) -> list:
        res = []
        for i in range(1, numRows+1):
            tmp = [0] * i
            tmp[0] = 1
            tmp[-1] = 1
            res.append(tmp)
        
        for i in range(2, numRows):
            for j in range(1, i):
                res[i][j] = res[i-1][j-1] + res[i-1][j]

        return res

if __name__ == '__main__':
    obj = Solution()
    print(obj.generate(1))
        