import numpy

string = input()
num_rows = int(input())
size = int(len(string))
num_cols = int(size)

list = numpy.zeros((num_rows,num_cols),dtype = str)
#list = [ [''] * num_cols for i in range(num_rows)]
print(list)

cur_row = 0
cur_col = 0
cur_index = 0
row_flag = False
col_flag = True
list[0][0] = string[0]
print(size)
while cur_index < size - 1:
        if col_flag:
            for i in range(num_rows - 1):
                print(cur_index)
                print(list)
                cur_row += 1
                cur_index += 1
                if cur_index < size:
                    list[cur_row][cur_col] = string[cur_index]
            col_flag = False
            row_flag = True
        elif row_flag:
            for j in range(num_rows - 2):
                print(cur_index)
                print(list)
                cur_row -= 1
                cur_col += 1
                cur_index += 1
                if cur_index < size:
                    list[cur_row][cur_col] = string[cur_index]
            cur_row = 0  
            cur_col += 1
            cur_index += 1
            if cur_index < size:
                list[cur_row][cur_col] = string[cur_index]
            row_flag = False
            col_flag = True
print(list)
token = ''
for i in list:
    for j in i:
        if j != '':
            token += j
print(token)