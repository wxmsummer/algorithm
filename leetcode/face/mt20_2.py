def fun():
    n = int(input())
    i = 0
    res = []
    while i < n:
        line = list(input().split(" "))
        for j in range(n):
            if line[j] not in res:
                res.append(line[j])
                break
        i += 1
    return (" ".join(res))


if __name__ == '__main__':
    print(fun())