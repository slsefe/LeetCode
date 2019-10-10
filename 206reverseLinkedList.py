'''
leetcode 206 反转链表
1->2->3->4->5->null经过反转得到5->4->3->2->1->null
使用迭代和递归两种解法。
迭代法：遍历链表，使用prev指针和curr指针改变结点顺序
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def reverseList_v1(self, head: ListNode) -> ListNode:
        '''迭代解法'''
        prev = ListNode(None)
        while head != None:
            curr = head.next
            head.next = prev
            prev = head
            head = curr
        return prev

    def reverseList_v2(self, head: ListNode) -> ListNode:
        '''递归解法'''
        if not head or not head.next:
            return head
        start = self.reverseList_v2(head.next)
        head.next.next = head
        head.next = None
        return start