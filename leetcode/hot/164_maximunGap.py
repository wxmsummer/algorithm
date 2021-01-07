class Solution:
    # 直接排序后遍历取值，排序复杂度O(nlgn)
    def maximumGap(self, nums: list) -> int:
        if len(nums) < 2:
            return 0
        nums.sort()
        max_gap = 0
        for i in range(1, len(nums)):
            max_gap = max(nums[i] - nums[i-1], max_gap)

        return max_gap

    # 桶排序
    def maximumGap(self, nums: list) -> int:
        if len(nums) < 2:
            return 0
        max_, min_ = max(nums), min(nums)
        print('max_:', max_, 'min_:', min_)
        if max_ == min_:
            return 0
        max_gap = 0
        length = len(nums)
        bucket_len = max(1, (max_ - min_) // (length - 1))
        bucket_num = (max_ - min_) // bucket_len + 1

        buckets = [[] for _ in range(bucket_num)]

        for i in range(length):
            loc = (nums[i] - min_) // bucket_len
            buckets[loc].append(nums[i])

        print('buckets:', buckets)

        pre_max = max(buckets[0])
        for i in range(1, bucket_num):
            if buckets[i]:
                max_gap = max(max_gap, min(buckets[i]) - pre_max)
            if buckets[i]:
                pre_max = max(buckets[i])

        return max_gap


if __name__ == '__main__':
    obj = Solution()
    print(obj.maximumGap([10]))
    print(obj.maximumGap([3,6,9,1,20]))
    print(obj.maximumGap([1,1,1,1,5,5,5,5,5]))