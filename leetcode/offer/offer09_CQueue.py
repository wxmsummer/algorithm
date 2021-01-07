# 双栈实现队列
class CQueue:

    def __init__(self):
        self.A = []

    def appendTail(self, value: int) -> None:
        self.A.append(value)

    def deleteHead(self) -> int:
        if self.B:
            return self.B.pop()
        if not self.A:
            return -1
        # 将A的元素放入B中，实现队列效果
        while self.A:
            self.B.append(self.A.pop())
        return self.B.pop()

    # def deleteHead(self) -> int:
    #     if not self.A:
    #         return -1
    #     return self.A.pop(0)

    # def deleteHead(self) -> int:
    # if not self.A:
    #     return -1
    # num = self.A[0]
    # del self.A[0]
    # return num

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()




