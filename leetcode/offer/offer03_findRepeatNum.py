# 数组中重复的数字

def findRepeatNumber():
    numList = [2, 3, 1, 0, 2, 5, 3]
    # 使用集合
    tempSet = set()
    for i in range(len(numList)):
        tempSet.add(numList[i])
        if len(tempSet) < i+1:
            return numList[i]


if __name__ == '__main__':
    print(findRepeatNumber())