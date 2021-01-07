'''list = []
token = '' '''
string = input()
a=-2**31
b=2**31-1
print(a,b)
if int(string) < -2**31 or int(string) > 2**31 - 1:
    print(0)
if string[0] == '-':
    result = string[1:][::-1]
    result = -int(result)
    if int(result) < -2**31 or int(result) > 2**31 - 1:
        print(0)
else:
    result = string[::-1]
    result = int(result)
    if int(result) < -2**31 or int(result) > 2**31 - 1:
        print(0)
print(result)
'''for i in string:
    list.append(i)
list.reverse()
for i in list:
    token += i
integer = int(token)
print(integer)'''