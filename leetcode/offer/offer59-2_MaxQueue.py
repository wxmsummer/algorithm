# 队列的最大值

import queue

class MaxQueue:
    
    def __init__(self):
        self.queue = queue.Queue()
        self.deque = queue.deque()

    def max_value(self) -> int:
        return self.deque[0] if self.deque else -1

    def push_back(self, value: int) -> None:
        # 留下大的数，保证辅助队列里的数递减
        while self.deque and self.deque[-1] < value:
            self.deque.pop()
        self.deque.append(value)
        self.queue.put(value)

    def pop_front(self) -> int:
        if not self.deque:
            return -1
        ans = self.queue.get()
        if ans == self.deque[0]:
            self.deque.popleft()
        return ans

# 双数组实现
class MaxQueue:
    
    def __init__(self):
        self.A, self.B = [], []

    def max_value(self) -> int:
        return self.B[0] if self.B else -1

    def push_back(self, value: int) -> None:
        self.A.append(value)
        while self.B and self.B[-1] < value:
            self.B.pop()
        self.B.append(value)

    def pop_front(self) -> int:
        if not self.A:
            return -1
        val = self.A.pop(0)
        if val == self.B[0]:
            self.B.pop(0)
        return val


# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()