# 替换空格

def replaceSpace(s: str) -> str:
    new_s = ''
    for i in range(len(s)):
        if s[i] == ' ':
            new_s += '%20'
        else:
            new_s += s[i]
    return new_s

if __name__ == '__main__':
    print(replaceSpace('aa a'))
