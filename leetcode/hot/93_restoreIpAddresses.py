# 求某数的正整数加和

class Solution:
    def restoreIpAddresses(self, target: int) -> list:
        def recur(tmp, target):
            if target == 0:
                res.append(tmp[:])
            
            if target < 0 :
                return

            if tmp:
                last = tmp[-1]
            else:
                last = 1

            # 这样保证后加的数大于前面的数
            for i in range(last, target+1):
                tmp.append(i)
                recur(tmp, target-i)
                tmp.pop()

        res = []
        recur([], target)
        return res

if __name__ == '__main__':
    obj = Solution()
    print(obj.restoreIpAddresses(6))