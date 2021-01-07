class Solution:
    def multiply(self, num1:str, num2:str) -> str:
        len1, len2 = len(num1), len(num2)
        res = [0] * (len1 + len2 - 1)

        for i in range(len1-1, -1, -1):
            for j in range(len2-1, -1, -1):
                num = int(num1[i]) * int(num2[j])
                res[i+j] += num

        print('res:', res)

        i = len(res) - 1
        while i > 0:
            res[i-1] += res[i] // 10
            res[i] = res[i] % 10
            i -= 1
            print('res:', res)
        
        i = 0
        while i < len(res)-1:
            if res[i] != 0:
                break
            res[i] = ''
            i += 1

        res = ''.join(str(i) for i in res)
        # return str(int(res))
        return res

if __name__ == '__main__':
    obj = Solution()
    print(obj.multiply('9', '9'))
    print(obj.multiply('123', '456'))
    print(obj.multiply('0', '123456'))