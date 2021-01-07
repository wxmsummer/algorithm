# 最靠近原点的k个点
class Solution:
    # 使用堆进行操作
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        q = [(-x** 2 - y**2, i) for i, (x, y) in enumerate(points[:K])]
        heapq.heapify(q)

        stack = []
        for i in range(len(points)):
            x, y = points[i]
            distant = -x**2 - y**2
            heapq.heappushpop(q, (distant, i))
        
        ans = [points[i] for (_, i) in q]
        return ans
