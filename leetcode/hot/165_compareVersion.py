# 165.比较版本号

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        list1, list2 = version1.split('.'), version2.split('.')
        
        # 去除前缀0
        list1, list2 = list(map(int, list1)), list(map(int, list2))

        # 去除后置0
        while list1 and list1[-1] == 0:
            list1.pop()
        while list2 and list2[-1] == 0:
            list2.pop()

        # print('list1:', list1)
        # print('list2:', list2)

        len1, len2 = len(list1), len(list2)
        i = 0
        # 逐个比较
        while i < len1 and i < len2:
            if list1[i] > list2[i]:
                return 1
            elif list1[i] < list2[i]:
                return -1
            i += 1
        # 如果前部分都相同 则看长度
        if len1 > len2:
            return 1
        elif len1 < len2:
            return -1
        else:
            return 0

if __name__ == '__main__':
    obj = Solution()
    print(obj.compareVersion('1', '0'))
    # print(obj.compareVersion('1.0.0', '1.0'))
    # print(obj.compareVersion('1.01', '1.001'))
    # print(obj.compareVersion('0.1', '1.1'))
    # print(obj.compareVersion('1.0.1', '1'))
    # print(obj.compareVersion('7.5.2.4', '7.5.3'))