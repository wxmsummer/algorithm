# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a, b = headA, headB
        while a != b:
            print('a:',a)
            print('b:',b)
            if a:
                a = a.next
            else:
                a = headB
            if b:
                b = b.next
            else:
                b = headA                
        return a