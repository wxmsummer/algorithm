class Solution:
    def subsets(self, nums: list) -> list:
        res = []
        # 通过寻找长度为0，1，2 ... len(nums) 的子集，找全所有子集
        for i in range(len(nums)+1):
            res += self.combine(nums, i)
        return res

    def combine(self, nums: list, k: int) -> list:
        # 回溯法，idx为当前元素，cur为当前解
        def backtrack(idx, cur):
            # 如果当前解符合要求，就加入解集
            if len(cur) == k:
                res.append(cur[:])
            # 遍历当前位置后面的元素
            for i in range(idx, len(nums)):
                print('cur:', cur)
                cur.append(nums[i])
                # 开启下一层判断
                backtrack(i+1, cur)
                # 回溯
                cur.pop()
        res = []
        # 注意这里是从1开始
        backtrack(0, [])
        return res

class Solution:
    def subsets(self, nums):		
        if not nums:
            return []
        res = []
        n = len(nums)

        def helper(idx, temp_list):
            res.append(temp_list)
            for i in range(idx, n):
                helper(i + 1, temp_list + [nums[i]])

        helper(0, [])
        return res

if __name__ == '__main__':
    obj = Solution()
    print(obj.subsets([1,2,3]))