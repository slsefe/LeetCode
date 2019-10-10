'''
leetcode 061 旋转链表
给定一个链表，旋转链表，将链表的每个结点向右移动k个位置，其中k为非负数。
思路：1.遍历链表，将尾结点指向头结点，构造循环链表，同时得到链表长度n；2.从链表头部开始遍历，使用快慢指针找到倒数第n+1个节点；3.断开倒数第n+1个节点并指向空，头指针指向倒数第n个节点。时间复杂度O(n)，空间复杂度O(1)。
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # 空链表或单元素链表
        if not head or not head.next:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        tmp = dummy
        # 遍历一次链表，得到链表长度
        length = 0
        while tmp.next:
            length += 1
            tmp = tmp.next
        # 快慢指针找到链表倒数第n+1个节点（n可能大于链表长度）
        slow, fast = dummy, dummy
        for _ in range(k % length):
            fast = fast.next
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        # 快指针指向head，新的头结点为慢指针的下一个节点，慢指针指向空
        fast.next = head
        head = slow.next
        slow.next = None
        return head
