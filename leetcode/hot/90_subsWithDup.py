# 求子集2
# nums可能包含重复元素

class Solution:
    def subsetsWithDup(self, nums: list) -> list:
        def backTrack(start, tmp):
            res.append(tmp[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                tmp.append(nums[i])
                backTrack(i+1, tmp)
                tmp.pop()
        
        nums.sort()
        res = []
        backTrack(0, [])
        return res

if __name__ == '__main__':
    obj = Solution()
    print(obj.subsetsWithDup([1,2,2,2,2]))