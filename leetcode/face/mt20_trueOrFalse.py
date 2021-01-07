
def solution():
    word_list = input().split(" ")
    A , B = [], []
    dic = {'true':1, 'false':0}
    dic2 = {1:'true', 0:'false'}
    i = 0
    while i < len(word_list):
        if word_list[i] == 'true':
            A.append(dic['true'])
        elif word_list[i] == 'false':
            A.append(dic['false'])
        elif word_list[i] == 'or':
            if i == 0 or i == len(word_list) - 1:
                print('error')
                return
            elif word_list[i-1] not in ['true', 'false'] or word_list[i+1] not in ['true', 'false']:
                print('error')
                return
            B.append('or')
        elif word_list[i] == 'and':
            if i == 0 or i == len(word_list) - 1:
                print('error')
                return
            elif word_list[i-1] not in ['true', 'false'] or word_list[i+1] not in ['true', 'false']:
                print('error')
                return
            i += 1
            A.append(A.pop() and dic[word_list[i]])
        i += 1
        print('A:', A, 'B:', B)

    while B:
        B.pop()
        tmp1 = A.pop()
        tmp2 = A.pop()
        A.append(tmp1 or tmp2)
        print('A:', A, 'B:', B)
    if len(A) != 1:
        print('error')
        return
    print(dic2[A.pop()])

if __name__ == '__main__':
    solution()