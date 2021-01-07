# 删除链表节点

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        
        temp = head

        if temp.val == val:
            if not temp.next:
                return None
            return temp.next

        while temp.next:
            if temp.next.val == val:
                if not temp.next.next:
                    temp.next = None
                    return head
                temp.next = temp.next.next
                return head
            temp = temp.next

class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        # 若要删除的节点为首节点，直接返回首节点的next
        if head.val == val :
            return head.next
        
        pre, cur = head, head.next
        # 双指针，循环往后
        while cur and cur.val != val:
            pre, cur = cur, cur.next
        # 如果发现要删除的节点，则进行删除
        if cur:
            pre.next = cur.next
        return head