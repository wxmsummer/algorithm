# 删除链表的倒数第N个节点

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None

class Solution():
    def removeNthFromEnd(self, head:ListNode, n:int) -> ListNode:

        slow, fast = head, head
        # fast先走n步
        for i in range(0, n):
            fast = fast.next
        
        # 说明fast走到尽头，也说明要删除的就是头节点
        if not fast:
            return head.next

        # fast和slow同时走，直到fast走到尽头
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        
        return head