list = [1,3]
number = 3
if number <= list[0]:
    print(0)
elif number > list[-1]:
    print(len(list))
else:
    for i in range(len(list) - 1):
        if list[i] <= number <= list[i+1]:
            print(i+1)
            break