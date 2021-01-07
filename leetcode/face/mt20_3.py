def fun():
    n, x, y = list(map(int, input().split(" ")))
    dic = {}
    for i in range(1, n+1):
        dic[i] = []

    for i in range(n-1):
        u, v = list(map(int, input().split(" ")))
        dic[u].append(v)
        dic[v].append(u)
    
    print('dic:', dic)

    def lastOrder(pre: int, cur: int):
        global max_
        for i in range(len(dic[cur])):
            if dic[cur][i] == pre:
                print('continue...')
                continue
            max_ = max(max_, lastOrder(cur, dic[cur][i]))
        print('max_:', max_)
        return max_ + 1

    def get_deep(pre:int, cur:int):
        for i in range(len(dic[cur])):
            if dic[cur][i] == pre:
                print('continue...')
                continue
            deep += 1

    lastOrder(0, 1)
    return max_

if __name__ == '__main__':
    max_ = 0
    print(fun())
