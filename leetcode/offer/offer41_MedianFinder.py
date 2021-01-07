# 求中位数

# 排序法
class MedianFinder:
    
    def __init__(self):
        self.numList = []


    def addNum(self, num: int) -> None:
        self.numList.append(num)

    def findMedian(self) -> float:
        numList = self.numList
        if not numList:
            return None

        numList.sort()
        length = len(numList)
        mid = int(length / 2)

        if length % 2 == 0:
            return float( (numList[mid-1] + numList[mid]) / 2)
        else:
            return numList[mid]

# 小顶堆 + 大顶堆
class MedianFinder:
    
    def __init__(self):
        self.A = []
        self.B = []

    # A为小顶堆，保存较大的一半数；B为大顶堆，保存较小的一半数
    # python中的heap为小顶堆，则大顶堆中存储num的相反数即可
    def addNum(self, num: int) -> None:
        # 添加数时，要保证A保存较大的一半
        # 如果A数量比B大1，则将(A和num中)最小的数插入B中，此时要先将num插入A，再从A的堆顶取出最小的数，将其插入B
        if len(self.A) != len(self.B):
            heappush(self.A, num)
            heappush(self.B, -heappop(self.A))
        # 如果A B数量相等，则将(B和num中)最大的数插入A中，此时要先将num插入B，再从B的堆顶取出最大的数，将其插入A
        else:
            heappush(self.B, -num)
            heappush(self.A, -heappop(self.B))

    def findMedian(self) -> float:
        # 奇数返回A[0]，偶数返回均值
        return self.A[0] if len(self.A) != len(self.B) else (self.A[0] - self.B[0]) / 2.0 

if __name__ == '__main__':
    obj = MedianFinder()
    print(obj.findMedian())
    obj.addNum(3)
    print(obj.findMedian())
    obj.addNum(2)
    print(obj.findMedian())
