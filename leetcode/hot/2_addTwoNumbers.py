# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.NumToList(self.listToNum(l1) + self.listToNum(l2))

    def listToNum(self, l: ListNode) -> int:
        count, res = 0, 0
        while l:
            res += l.val * (10 ** count)
            count += 1
            l = l.next
        return res
    
    def NumToList(self, num:int) -> ListNode:
        temp = ListNode(0, None)
        temp.val = num % 10
        num //= 10
        head = temp
        print('head:', head.val)
        while num != 0:
            node = ListNode(0, None)
            node.val = num % 10
            num //= 10
            temp.next = node
            temp = node
            print('head:', head.val)
        return head

    def PrintList(self, l: ListNode):
        count = 0
        while l:
            print("val:", l.val)
            l = l.next
            
if __name__ == '__main__':
    obj = Solution()
    # print(obj.NumToList(807).val)
    obj.PrintList(obj.NumToList(807))