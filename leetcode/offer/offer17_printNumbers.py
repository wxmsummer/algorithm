class Solution:
    def printNumbers(self, n: int) -> list:
        numList = []
        for i in range (1, 10 ** n):
            numList.append(i)
        return numList

if __name__ == '__main__':

    obj = Solution()
    print(obj.printNumbers(3))  