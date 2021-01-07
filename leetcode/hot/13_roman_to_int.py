dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 'IV':-2, 'IX': -2, 'XL':-20, 'XC':-20, 'CD':-200, 'CM':-200}
number = 0
string = input()
for i in range(len(string)):
    token = ''
    number += dict[string[i]]
    if i < len(string)-1:
        token = string[i] + string[i+1]
    if token in dict:
        number += dict[token]
print(number)