char_list = ["flower","flow","flight"]
s = ''
for i in zip(*char_list):
    if len(set(i)) == 1:
        s += i[0]
    else:
        break
print(s) 