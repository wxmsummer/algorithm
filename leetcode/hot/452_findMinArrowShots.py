# 射气球

class Solution:
    def findMinArrowShots(self, points: list) -> int:
        if not points:
            return 0
        # 先按左端点进行排序
        points.sort(key=lambda x:x[0])
        print('ponits:',points)
        length = len(points)
        # 
        right = points[0][1]
        count = 1
        for i in range(1, length):
            print('right:', right)
            # 如果发现右端点更小的，则更新right
            if points[i][1] < right:
                right = points[i][1]
            # 如果左端点小于等于right，则看下一区间
            if points[i][0] <= right:
                continue
            # 如果左端点大于right，则更新right，且count++
            elif points[i][0] > right:
                count += 1
                right = points[i][1]
        return count

if __name__ == '__main__':
    obj = Solution()
    # print(obj.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))
    # print(obj.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))
    print(obj.findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]))
    # print(obj.findMinArrowShots([[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]))