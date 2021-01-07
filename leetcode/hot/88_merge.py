class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        if not nums1:
            return nums2
        if not nums2:
            return nums1
        i, j, cur = m-1, n-1, m+n-1
        while i >= 0 and j >= 0:
            if nums1[i] <= nums2[j]:
                nums1[cur] = nums2[j]
                j -= 1
                cur -= 1
            else:
                nums1[cur] = nums1[i]
                i -= 1
                cur -= 1
        
        if i < 0:
            while j >= 0:
                nums1[cur] = nums2[j]
                cur -= 1
                j -= 1

        return nums1

if __name__ == '__main__':
    obj = Solution()
    print(obj.merge([1,2,3,0,0,0], 3, [2,5,6], 3))