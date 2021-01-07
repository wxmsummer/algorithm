temp = []
max_length = 0
result = input()
for i in range(len(result)):
    if result[i] in temp:
        index = temp.index(result[i])
        for j in range(index + 1):
            del(temp[0])
        temp.append(result[i])
        max_length = max(max_length, len(temp))
        print(temp)
        continue
    else:
        temp.append(result[i])
        max_length = max(max_length, len(temp))
        print(temp)
        continue
print('temp:',temp)
print('the max length is:',max_length)