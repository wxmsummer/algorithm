nums = [0,0,1,1,1,2,2,3,3,4]
'''nums = list(set(nums))
print(nums)'''
index = 0
for i in range(len(nums)-1):
    if nums[index] == nums[index + 1]:
        del nums[index]
    else:
        index += 1
    print(nums)