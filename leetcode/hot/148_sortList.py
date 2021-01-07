# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        # 利用快慢指针找出中间节点
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        mid = slow.next
        slow.next = None
        # 对左部分链表和右部分链表进行递归
        left, right = self.sortList(head), self.sortList(mid)
        h = res = ListNode(0)
        # 对左部分和右部分进行归并
        while left and right:
            if left.val < right.val:
                h.next = left
                left = left.next
            else:
                h.next = right
                right = right.next
            h = h.next
        # 链接剩下的
        h.next = left if left else right
        return res.next