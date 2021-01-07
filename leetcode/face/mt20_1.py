def fun():
    n = input()
    s = input()
    i, j = 0, len(s) - 1
    while True:
        if s[i] == 'M':
            head_M = True
        if head_M and s[i] == 'T':
            break
        i += 1
    while True:
        if s[j] == 'T':
            tail_T = True
        if tail_T and s[j] == 'M':
            break
        j -= 1
    return s[i+1:j]


if __name__ == '__main__':
    print(fun())