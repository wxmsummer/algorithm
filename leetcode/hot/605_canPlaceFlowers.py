# 605.种花问题

from typing import List

class Solution:
    # 模拟法，如果该位置、该位置的前一个位置、该位置的后一个位置没种，就种上
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        count = 0
        for i in range(length):
            # 注意数组越界
            if flowerbed[i] == 1 or (i > 0 and flowerbed[i-1]==1) or (i < length - 1 and flowerbed[i+1] == 1):
                continue
            else:
                flowerbed[i] = 1
                count += 1
        print('flower:', flowerbed)
        return True if count >= n else False


if __name__ == '__main__':
    obj = Solution()
    print(obj.canPlaceFlowers([1,0,0,0,1], 1)) 
    print(obj.canPlaceFlowers([1,0,0,0,1], 2))   
    print(obj.canPlaceFlowers([1,0,0,0,0,1], 2))   