# 包含min函数的栈

class MinStack:

    def __init__(self):
        self.A, self.B = [], []

    # 使用辅助栈B，逐个存储弹栈时的min元素
    def push(self, x: int) -> None:
        self.A.append(x)
        # 如果B为空或x比栈顶元素大，才入辅助栈
        if not self.B or self.B[-1] >= x:
            self.B.append(x)

    def pop(self) -> None:
        # 如果A弹出的元素和B栈顶元素相等，则也需要弹出B栈顶元素
        if self.A.pop() == self.B[-1]:
            self.B.pop()

    def top(self) -> int:
        return self.A[-1]

    def min(self) -> int:
        return self.B[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()