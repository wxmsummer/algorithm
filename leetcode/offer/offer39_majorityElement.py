class Solution:
    # def majorityElement(self, nums: list) -> int:
    #     dic = {}
    #     length = len(nums)
    #     for i in range(length):
    #         num = nums[i]
    #         if num in dic:
    #             dic[num] += 1
    #         else:
    #             dic[num] = 1
    #         if dic[num] > length / 2:
    #             return num

    def majorityElement(self, nums: list) -> int:
        votes, count = 0, 0
        for num in nums:
            if votes == 0:
                x = num
            if num == x:
                votes += 1
            else:
                votes -= 1
        return x


if __name__ == '__main__':
    
    obj = Solution()
    print(obj.majorityElement([1, 2, 2, 3]))