#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 
# @param n long长整型 正整数n
# @return long长整型
#
class Solution:
    def intReplace(self , n ):
        count1, count2 = 0, 0
        n1, n2 = n, n
        while n1 != 1:
            if n1 % 2 == 0:
                n1 = n1 / 2
                count1 += 1
            else:
                n1 += 1
                count1 += 1

        while n2 != 1:
            if n2 % 2 == 0:
                n2 = n2 / 2
                count2 += 1
            else:
                n2 -= 1
                count2 += 1

        return min(count1, count2)
        # write code here

if __name__ == '__main__':
    obj = Solution()
    print(obj.intReplace(10))