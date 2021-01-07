class Solution:
    def addBinary(self, a: str, b: str) -> str:
        len_a, len_b = len(a), len(b)
        max_len = max(len_a, len_b)
        list_a, list_b = [0] * (max_len + 1), [0] * (max_len + 1)
        diff_a = max_len - len_a
        diff_b = max_len - len_b
        for i in range(len_a):
            list_a[1+ i+ diff_a] = int(a[i])
        for i in range(len_b):
            list_b[1+ i+ diff_b] = int(b[i])
        print('list_a:', list_a)
        print('list_b:', list_b)

        for i in range(max_len,-1, -1):
            list_b[i] = list_a[i] + list_b[i]

        for i in range(max_len,-1, -1):
            list_b[i-1] += list_b[i] // 2
            list_b[i] = list_b[i] % 2
        
        if list_b[0] == 0:
            return ''.join(str(i) for i in list_b[1:])
        else:
            return ''.join(str(i) for i in list_b)

if __name__ == '__main__':
    obj = Solution()
    print(obj.addBinary('10101', '111'))