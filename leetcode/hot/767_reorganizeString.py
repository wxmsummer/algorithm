# 重构字符串

import collections
import heapq

class Solution:
    def reorganizeString(self, S:str) -> str:
        if len(S) < 2:
            return S
        
        length = len(S)
        
        # 计算各字符出现的次数，key为字母，val为次数
        counts = collections.Counter(S)
        max_ = max(counts.items(), key=lambda x:x[1])[1]
        
        # 如果次数最多的大于一半，则无法重构
        if max_ > (length + 1) // 2:
            return ''
        
        # 由于是小顶堆，需要使用-x[1]
        queue = [(-x[1], x[0]) for x in counts.items()]
        heapq.heapify(queue)
        
        res = ''
        # 每次取剩余频率最大的两个字母拼接
        while len(queue) > 1:
            _, letter1 = heapq.heappop(queue)
            _, letter2 = heapq.heappop(queue)
            res += letter1
            res += letter2
            counts[letter1] -= 1
            counts[letter2] -= 1
            if counts[letter1] > 0:
                heapq.heappush(queue, (-counts[letter1], letter1))
            if counts[letter2] > 0:
                heapq.heappush(queue, (-counts[letter2], letter2))

        if queue:
            res += queue[0][1]

        return res

if __name__ == '__main__':
    obj = Solution()
    print(obj.reorganizeString('vvvlo'))    