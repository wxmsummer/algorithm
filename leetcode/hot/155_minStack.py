# 最小栈

class MinStack:
    
    def __init__(self):
        self.A, self.B = [], []
        """
        initialize your data structure here.
        """

    def push(self, x: int) -> None:
        self.A.append(x)
        # 如果辅助栈空，则加入x
        if not self.B:
            self.B.append(x)
        else:
            # 当辅助栈非空时，判断新入元素是否小于等于辅助栈末尾元素
            # 注意等号要取
            if x <= self.B[-1]:
                self.B.append(x)

    def pop(self) -> None:
        num = self.A.pop()
        if num == self.B[-1]:
            self.B.pop()

    def top(self) -> int:
        return self.A[-1]

    def getMin(self) -> int:
        return self.B[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()