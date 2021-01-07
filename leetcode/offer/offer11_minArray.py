# 旋转数组的最小数字
class Solution:
    def minArray(self, numbers:list) -> int:
        i = 0
        j = len(numbers) - 1
        # 采用二分法，寻找旋转点
        while(i < j):
            m = (i + j) // 2
            if numbers[m] > numbe3rs[j]:
                i = m + 1
            elif numbers[m] < numbers[j]:
                j = m
            else: 
                return min(numbers[i:j])
        return numbers[i]

if __name__ == '__main__':

    obj = Solution()
    numbers = [3, 4, 5, 6, 1, 2]
    print(obj.minArray(numbers))