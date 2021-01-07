# 翻转对

class Solution:
    # 暴力解法
    def reversePairs(self, nums: list) -> int:
        length = len(nums)
        count = 0
        for i in range(length):
            for j in range(i+1, length):
                if nums[i] > 2 * nums[j]:
                    count += 1

        return count

    # 归并排序，O(nlogn)
    def reversePairs(self, nums: list) -> int:
        n = len(nums)
        tmp = [0] * n
        return self.mergeSort(nums, tmp, 0, n-1)
    
    # [left,right]闭区间
    def mergeSort(self, nums, tmp, left, right):
        if left >= right:
            return 0
        
        mid = (left + right) // 2
        count = self.mergeSort(nums, tmp, left, mid) + self.mergeSort(nums, tmp, mid+1, right)
        i, j = left, mid + 1
        pos = left
        print('left:', nums[left:mid+1], 'right:', nums[mid+1:right+1])
        
        # 对重要翻转对进行计数
        for i in range(left, mid+1):
            while j <= right and nums[i] > 2*nums[j]:
                count += (mid + 1 - i)
                j += 1
        
        i, j = left, mid + 1
        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                tmp[pos] = nums[i]
                i += 1
            else:
                tmp[pos] = nums[j]
                j += 1
            pos += 1
        
        for k in range(i, mid+1):
            tmp[pos] = nums[k]
            pos += 1
        for k in range(j, right+1):
            tmp[pos] = nums[k]
            pos += 1
        nums[left:right+1] = tmp[left:right+1]
        return count

if __name__ == '__main__':
    obj = Solution()
    # print(obj.reversePairs([1,3,2,3,1]))
    # print(obj.reversePairs([2,4,3,5,1]))
    print(obj.reversePairs([7,5,6,4,1,2,3,8]))
