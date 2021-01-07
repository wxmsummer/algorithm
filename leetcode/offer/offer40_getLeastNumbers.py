# 最小的k个数
class Solution:
    # 排序法
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        return arr[:k]

class Solution:
    # 使用堆解决 使用大根堆实时维护前k小值
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return list()

        hp = [-x for x in arr[:k]]
        heapq.heapify(hp)
        for i in range(k, len(arr)):
            # 如果当前遍历到的数比堆顶小
            # 则替换堆顶元素
            if -hp[0] > arr[i]:
                heapq.heappop(hp)
                heapq.heappush(hp, -arr[i])
        ans = [-x for x in hp]
        return ans


if __name__ == '__main__':
    
    obj = Solution()
    print(obj.getLeastNumbers([1, 2, 2, 3]))