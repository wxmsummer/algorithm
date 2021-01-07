# 链表反转

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = None
        pre = head
        while pre:
            temp = pre.next # 借助temp节点，方便pre和cur移动
            pre.next = cur
            cur = pre
            pre = temp
        return cur
