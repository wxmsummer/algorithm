class Solution:
    def merge(self, intervals: list) -> list:
        intervals.sort(key=lambda x:x[0])
        length = len(intervals)
        res = []
        res.append(intervals[0])
        for i in range(length):
            if res[-1][1] < intervals[i][0]:
                res.append(intervals[i])
            else:
                res[-1][1] = max(res[-1][1], intervals[i][1])

        return res


if __name__ == '__main__':
    obj = Solution()
    print(obj.merge([[1,3],[2,6],[8,10],[15,18]]))