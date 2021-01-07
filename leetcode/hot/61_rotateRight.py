# 旋转链表

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 先求出长度，然后求出旋转后的新head，再进行拼接
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # 如果链表为空或者k为0，直接返回head
        if not head or k == 0:
            return head
        length = self.getLen(head)
        pre = ListNode(0, head)
        new_head = head
        count = 0
        k = k % length

        # 如果k为0，说明旋转后和原来一样
        if k == 0:
            return head
        
        # 找到新head
        while count < length - k:
            pre = pre.next
            new_head = new_head.next
            count += 1
        
        # 求出tail尾节点
        tail = head
        while tail.next:
            tail = tail.next

        # 进行旋转
        tail.next = head
        pre.next = None
        return new_head

    # 求链表长度
    def getLen(self, head:ListNode) -> int:
        count = 0
        while head:
            head = head.next
            count += 1
        return count


