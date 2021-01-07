# 小镇法官

class Solution:
    # 使用字典保存投票信息
    def findJudge(self, N: int, trust: list) -> int:
        if N == 1 and not trust:
            return 1
        elif not trust:
            return -1
        dic = {}
        people_set = set()
        length = len(trust)
        for i in range(length):
            first = trust[i][0]
            second = trust[i][1]
            people_set.add(first)
            if second not in dic:
                dic[second] = set()
                dic[second].add(first)
            else:
                dic[second].add(first)

        if len(people_set) != N-1:
            return -1

        for k in dic:
            if len(dic[k]) != N-1:
                continue
            if dic[k] == people_set:
                return k
        
        return -1

    # 投票法
    def findJudge(self, N: int, trust: list) -> int:
        length = len(trust)
        votes = [0] * (N+1)
        for i in range(length):
            votes[trust[i][0]] -= 1
            votes[trust[i][1]] += 1
        
        print('votes:', votes)
        for i in range(1, N+1):
            if votes[i] == N-1:
                return i
        
        return -1


if __name__ == '__main__':
    obj = Solution()
    print(obj.findJudge(3, [[1,3],[2,3]]))
    print(obj.findJudge(3, [[1,3],[2,3],[3,1]]))
    print(obj.findJudge(1, []))
    print(obj.findJudge(4, [[1,3],[1,4],[2,3]]))