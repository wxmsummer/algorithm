'''height_list = [1,8,6,2,5,4,8,3,7]
#height_list = [1,2,1]
max_area = 0
length = len(height_list)
new_list = []
for i in range(0,length):
    for j in range(i+1,length):
        max_area = max(max_area, min(height_list[i],height_list[j]) * (j-i))
print(max_area)'''

# 盛最多水的容器
# 双指针法，

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j, res = 0, len(height) - 1, 0
        while i < j:
            if height[i] < height[j]:
                res = max(res, height[i] * (j - i))
                i += 1
            else:
                res = max(res, height[j] * (j - i))
                j -= 1
        return res
