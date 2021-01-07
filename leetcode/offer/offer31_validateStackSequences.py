# 栈的压入、弹出序列

class Solution:
    def validateStackSequences(self, pushed: list, popped: list) -> bool:
        newList = []
        # 直接模拟，每次入栈后，循环判断栈顶元素是否等于弹出序列的当前元素，将符合弹出序列顺序的栈顶元素全部弹出。
        for num in pushed:
            newList.append(num)
            while newList and newList[-1] == popped[0]:
                del newList[-1]
                del popped[0]
        return popped == []
        
class Solution:
    def validateStackSequences(self, pushed: list, popped: list) -> bool:
        stack, i = [], 0
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        return not stack
    
if __name__ == '__main__':
       obj = Solution()
       print(obj.validateStackSequences([2, 1, 0], [1, 2, 0] ))