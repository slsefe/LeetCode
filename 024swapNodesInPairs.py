'''
leetcode 24 两两交换链表中的结点
给定一个链表，两两交换其中相邻的结点，返回交换后的链表。
思路：遍历链表，每两个节点内部进行交换
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 头结点
        dummy = ListNode(-1)
        dummy.next = head
        # 遍历链表的指针
        tmp = dummy
        while tmp.next and tmp.next.next:
            # 内部交换节点
            left = tmp.next
            right = tmp.next.next
            # 交换两个节点
            left.next = right.next
            right.next = left
            # 和前驱指针连接
            tmp.next = right
            # 前驱指针后移两个节点
            tmp = tmp.next.next
        return dummy.next
