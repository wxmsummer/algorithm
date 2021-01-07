# 合并两个排序的链表

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp1, temp2 = l1, l2
        if not l1:
            return l2
        elif not l2:
            return l1

        # 选出新头
        if temp1.val > temp2.val:
            head = temp2
            temp2 = temp2.next
        else:
            head = temp1
            temp1 = temp1.next
        
        # 不断取出两个链表中较小的元素
        temp = head
        while temp1 and temp2:
            if temp1.val > temp2.val:
                temp.next = temp2
                temp2 = temp2.next
                temp = temp.next
            else:
                temp.next = temp1
                temp1 = temp1.next
                temp = temp.next

        # 链接剩下的元素
        if temp1:
            temp.next = temp1
        else:
            temp.next = temp2

        return head

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur = dum = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next, l1 = l1, l1.next
            else:
                cur.next, l2 = l2, l2.next
            cur = cur.next

        cur.next = l1 if l1 else l2
        return dum.next