from collections import defaultdict

class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> list:
        dic = defaultdict(list)
        # 遍历坐标
        for i in range(R):
            for j in range(C):
                distant = abs(r0-i) + abs(c0-j)
                dic[distant].append([i,j])
        print('dic:', dic)
        res = []

        # 对字典按照key进行排序
        for i in range(R+C):
            if i in dic:
                for v in dic[i]:
                    res.append(v)
        # for i in sorted(dic):
        #     for v in dic[i]:
        #         res.append(v)

        return res

if __name__ == '__main__':
    obj = Solution()
    print(obj.allCellsDistOrder(2,3,1,2))