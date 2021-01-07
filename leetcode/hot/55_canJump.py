class Solution:
    # 贪心法
    def canJump(self, nums: list) -> bool:
        length = len(nums)
        max_ = nums[0]
        i = 0
        while i < max_+1:
            print('max_:', max_)
            # 更新最大可走距离
            max_ = max(max_, nums[i] + i)
            i += 1
            # 如果发现可以走出，则直接返回
            if max_ >= length - 1:
                return True

        return False

if __name__ == '__main__':
    obj = Solution()
    print(obj.canJump([2,3,1,1,4]))
    print(obj.canJump([3,2,1,0,4]))
    print(obj.canJump([1,2,3]))
    print(obj.canJump([2,3,1,1,0,0,0,0,0,4]))