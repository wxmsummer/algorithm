temp_list = []
char_list = list(input())
for i in range(len(char_list)):
    if char_list[i] == '(' or char_list[i] == '[' or char_list[i] == '{':
        temp_list.append(char_list[i])
    if char_list[i] == ')' or char_list[i] == ']' or char_list[i] == '}':
        if temp_list == []:
            print('false0')
            break
        elif char_list[i] == ')':
            if temp_list[-1] == '(':
                temp_list.pop()
            else:
                print('false1')
                break            
        elif char_list[i] == ']':
            if temp_list[-1] == '[':
                temp_list.pop()
            else:
                print('false2')
                break
        elif char_list[i] == '}':
            if temp_list[-1] == '{':
                temp_list.pop()
            else:
                print('false3')
                break     
    print(temp_list)
if temp_list == []:
    print('true')

'''class Solution:
    def isValid(self, s):
        while '{}' in s or '()' in s or '[]' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return s == '' '''