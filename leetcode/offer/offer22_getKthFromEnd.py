# 链表中倒数第k个节点

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 先获取链表长度，然后遍历至第len-k个，返回
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        i = 0
        temp = head
        while i < self.getLen(head) - k:
            temp = temp.next
            i += 1
        return temp

    def getLen(self, head: ListNode) -> int:
        if head == None:
            return 0
        temp = head
        length = 1
        while temp.next:
            temp = temp.next
            length += 1
        return length

# 双指针，快指针先走k步
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        former, later = head, head
        for _ in range(k):
            former = former.next
        while former:
            former, later = former.next, later.next
        return later