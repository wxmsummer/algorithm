# 数字序列中某一位的数字

class Solution:
    # 三步走，确定n所在数字为几位数，确定该数字，确定n是该数字中哪一位
    def findNthDigit(self, n: int) -> int:
        # digit， start， count 用于确定数字为几位数
        digit, start,  count = 1, 1, 9
        # 算出n所在位数
        while n > count:
            n -= count
            start *= 10
            digit += 1
            # 比如2位数是 10-99，总共有90个，每个占两位，则为2*90；；3位数为3*900，以此类推
            count = 9 * start * digit
        # 计算num具体值，为在几位数中的第几个
        # 如12，101112，算出12范围为[5，6]，则12实际上是两位数中第 6-1 // 2 = 2个数
        num = start + (n-1) // digit
        # (n-1) % digit 用于算出在num中的下标，然后先换为str取出具体数，再换回int
        return int(str(num)[(n-1)%digit])

if __name__ == '__main__':
    obj = Solution()
    print(obj.findNthDigit(1000))