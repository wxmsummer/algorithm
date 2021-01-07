
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = 0
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # dummyHead用于指向头节点
        dummyHead = ListNode(0, None)
        dummyHead.next = head
        temp = dummyHead
        
        # 如果temp后只有一个节点或没有节点，则结束交换
        while temp.next and temp.next.next:
            # temp的下一个节点和temp的下下个节点进行交换
            node1, node2 = temp.next, temp.next.next
            temp.next = node2
            node1.next = node2.next
            node2.next = node1
            # 将temp往前调
            temp = node1
        
        # 返回新头
        return dummyHead.next