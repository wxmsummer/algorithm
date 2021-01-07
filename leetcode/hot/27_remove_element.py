nums = [0,1,2,2,3,0,4,2]
val = 2
index = 0
for i in range(len(nums)):
    if nums[index] == val:
        del nums[index]
    else:
        index += 1
print(nums)