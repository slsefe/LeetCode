'''
leetcode 876 链表中间节点
给定一个非空链表，返回其中间节点，若有两个中间节点，返回后一个中间节点。
解法：快慢指针法
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
        return slow