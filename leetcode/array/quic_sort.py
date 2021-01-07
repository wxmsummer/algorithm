class Solution:
    def quic_sort(self, nums:list):
        def quit(nums:list, l: int, r: int):
            if l < r:
                i, j = l, r
                x = nums[l]
                while i < j:
                    while i < j and nums[j] >= x:
                        j -= 1
                    if i < j:
                        nums[i] = nums[j]
                        i += 1

                    while i < j and nums[i] < x:
                        i += 1
                    if i < j:
                        nums[j] = nums[i]
                        j -= 1
                nums[i] = x
                quit(nums, l, i-1)
                quit(nums, i+1, r)
            return nums
        return quit(nums, 0, len(nums)-1)

if __name__ == '__main__':
    obj = Solution()
    print(obj.quic_sort([3,1,6,7,5,4,9]))