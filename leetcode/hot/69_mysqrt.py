class Solution:
    # def mySqrt(self, x: int) -> int:
    #     i = 0
    #     while i ** 2 <= x:
    #         i += 1
    #     return i - 1

    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        ans = 0
        while l <= r:
            mid = (l + r) // 2
            if mid ** 2 <= x:
                l = mid + 1
                ans = mid
            else:
                r = mid - 1
        return ans

if __name__ == '__main__':
    obj = Solution()
    print(obj.mySqrt(20))
    print(obj.mySqrt(4))