# 删除排序链表中的重复元素

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        dummy = ListNode('x', head)
        dummy.next = head
        pre, cur = dummy, head
        while cur:
            # 如果遇到相同值的节点，就走到下一个不同值的位置
            if cur.next and cur.next.val == cur.val:
                while cur.next and cur.next.val == cur.val:
                    cur = cur.next
                pre.next = cur
            # 如果都是值不同的，则直接移动pre和cur
            else:
                cur = cur.next
                pre = pre.next
            print('list:', dummy.next)
        # dummy.next 为新链表的头
        return dummy.next

