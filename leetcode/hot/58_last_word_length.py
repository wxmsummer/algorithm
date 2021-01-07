new_list = []
string_list = input().split(" ")
print(string_list)
for every in string_list:
    if every != '':
        new_list.append(every)
print(new_list)
if new_list == []:
    print(0)
else:
    print(len(new_list[-1]))
# return len(s.rstrip().split(" ")[-1])