from collections import defaultdict

class Solution:
    def fourSumCount(self, A: list, B: list, C: list, D: list) -> int:
        len_A, len_B, len_C, len_D = len(A), len(B), len(C), len(D)
        count = 0
        for i in range(len_A):
            for j in range(len_B):
                for k in range(len_C):
                    for l in range(len_D):
                        if A[i] + B[j] + C[k] + D[l] == 0:
                            count += 1
        return count

    
    # 哈希表存储，空间换时间
    def fourSumCount(self, A: list, B: list, C: list, D: list) -> int:
        dic = defaultdict(int)
        len_A, len_B, len_C, len_D = len(A), len(B), len(C), len(D)
        count = 0
        for i in range(len_A):
            for j in range(len_B):
                dic[A[i]+B[j]] += 1

        print('dic:', dic)

        for i in range(len_C):
            for j in range(len_D):
                tmp = -(C[i] + D[j])
                if tmp in dic:
                    count += dic[tmp]

        return count

if __name__ == '__main__':
    obj = Solution()
    # print(obj.fourSumCount(A = [ 1, 2], B = [-2,-1], C = [-1, 2], D = [ 0, 2]))
    print(obj.fourSumCount([-1,-1], [-1,1], [-1,1], [1,-1]))