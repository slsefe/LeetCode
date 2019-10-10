'''
leetcode 237 删除链表中的非末尾结点
给定链表中的某个非末尾结点，删除此节点。
注意不会给出链表的头结点，即不清楚给定结点之前的链表情况，给定链表中的一个非末尾结点，要求删除此结点。由于无法得到要删除结点的前驱结点，无法使用常规手段删除。采取修改待删除结点值的方式，将待删除的结点值修改为下一个节点（待删除节点非尾结点，下一个节点一定存在）的值，再删除下一个节点即可。
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next