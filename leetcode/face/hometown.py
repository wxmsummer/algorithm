
# 样例输入
# 3 1
# 2 3 1
# 5 4
# 1 2 1
# 3 4 0
# 2 5 1
# 3 2 1

# 样例输出
# 0
# 3
while 1:
    # 给input().split(" ") 里的每一个元素都做int运算
    N, M = list(map(int, input().split(" ")))
    print('N M:', N, M)
    res = []
    for i in range(M):
        a, b, c = map(int, input().split(" "))
        if c == 1:
            r = [a, b] if a < b else [b, a]
            res.append(r)
    s = set()
    s.add(1)
    res.sort()
    for i in res:
        if i[0] in s:
            s.add(i[1])
    print(len(s) - 1)