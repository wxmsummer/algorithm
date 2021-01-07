# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        pre = head
        cur = head.next
        while cur:
            if cur.val >= pre.val :
                pre = cur
                cur = cur.next
                continue
            node = ListNode(cur.val, None)
            cur = cur.next
            pre.next = cur
            print('head1:', head)
            head = self.insert(head, node)
            print('head:', head)
        return head

    def insert(self, head, node):
        if node.val < head.val:
            node.next = head
            return node
        tmp = head
        while tmp.next:
            if tmp.next.val > node.val:
                break
            else:
                tmp = tmp.next
        node.next = tmp.next
        tmp.next = node

        return head