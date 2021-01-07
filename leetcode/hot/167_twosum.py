from typing import List

class Solution:
    # 左右指针
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1
        
if __name__ == '__main__':
    obj = Solution()
    print(obj.twoSum([2,7,11,15], 9))