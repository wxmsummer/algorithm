# 数组中的逆序对

class Solution:
    # 暴力解法，会超时
    def reversePairs(self, nums: list) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[j] < nums[i]:
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
        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                tmp[pos] = nums[i]
                i += 1
            # 当左侧大于右侧时，count加上左侧剩余数量，表示构成的逆序对数量
            else:
                tmp[pos] = nums[j]
                print('count +=', (mid + 1 - i))
                count += (mid + 1 - i)
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
    print(obj.reversePairs([7,5,6,4,1,2,3,8]))