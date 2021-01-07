# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        
        if head:
            pre, slow, fast = None, head, head
            # 利用快慢指针找出中间节点
            while fast and fast.next:
                pre, slow, fast = slow, slow.next, fast.next.next
            if pre:
                pre.next = None
            root = TreeNode(slow.val)
            # 已经拆分为最小节点
            if slow == fast:
                return root
            root.left = self.sortedListToBST(head)
            root.right = self.sortedListToBST(slow.next)
            return root
            