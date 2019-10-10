'''
leetcode 203 删除链表中等于给定值的结点
考虑以下情况：空链表，单元素链表，待删除节点在链表头部，待删除节点在链表尾部，待删除节点连续出现，非空链表删除后为空链表
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # 空链表
        if not head:
            return head
        # 单个元素
        if not head.next:
            if head.val == val:
                return None
            else:
                return head
        # 多个元素
        # 找到第一个不等于目标值的结点（要删除元素在链表头部）
        while head and head.val == val:
            head = head.next
        prev = head
        # 删除头部元素后链表为空
        if not head or not head.next:
            return head
        curr = head.next
        while curr:
            if curr.val == val:
                prev.next = prev.next.next
                curr = curr.next
            else:
                prev = prev.next
                curr = curr.next
        return head
