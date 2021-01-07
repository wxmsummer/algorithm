nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [-6,-5,-4,-3,-2,-1,0]
'''
max_now = nums[0]
sum_now = nums[0]
for i in range(len(nums)):
    sum_now = nums[i]
    max_now = max(max_now,sum_now)
    for j in range(i+1,len(nums)):
        sum_now += nums[j]
        max_now = max(max_now,sum_now)
        #print(max_now,sum_now)
print(max_now)'''

temp = nums[0]
max_ = temp
n = len(nums)
for i in range(1,n):
    if temp > 0:
        max_ = max(max_, temp + nums[i])
        temp = temp + nums[i]
    else:
        max_ = max(max_, temp, temp + nums[i], nums[i])
        temp = nums[i]
    print(max_)
