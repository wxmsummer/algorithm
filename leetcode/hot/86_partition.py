# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 方法一 创建两个新链表，分别保存小的部分和大的部分
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head
        left_list = ListNode('x', None)
        tmp1 = left_list
        right_list = ListNode('x', None)
        tmp2 = right_list
        cur = head
        while cur:
            if cur.val < x:
                tmp1.next = ListNode(cur.val, None)
                tmp1 = tmp1.next
            else:
                tmp2.next = ListNode(cur.val, None)
                tmp2 = tmp2.next
            cur = cur.next
            print('left:', left_list)
            print('right:', right_list)
        
        tmp1.next = right_list.next
        return left_list.next

    # 方法二 原地链接
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head
        dummy = ListNode('x', head)
        tmp, pre, cur = head, head, head.next
        while cur:
            # 如果大于，就直接往下
            if cur.val >= x:
                pre = pre.next
                cur = cur.next
            else:
                # 如果小部分的最右端和pre相等，且当前值小于x，则也直接往下
                if tmp == pre:
                    tmp = tmp.next
                    pre = pre.next
                    cur = cur.next
                # 否则就把当前值插入到小部分的最右端
                else:
                    pre.next = cur.next
                    cur.next = tmp.next
                    tmp.next = cur
                    tmp = tmp.next
                    cur = pre.next
        return dummy.next

