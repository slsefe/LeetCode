'''
leetcode 2: 两数相加

给定两个用非空链表逆序表示的两个整数，每个节点表示一位数字，将这两个链表表示的整数相加，返回一个链表表示他们的和。如`(2->4->3)+(5->6->4)=(7->0->8)`

思路：遍历链表，逐位相加，设置进位标志，构造新链表，最后判断是否有进位。

需要考虑的特殊情况：
1. 两个链表长度不相同的情况
2. 相加结果有进位的情况，需要再增加一个值为1的结点
'''
class ListNode(object):
    '''
    single-linked list
    '''
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''用链表表示的数字相加
        设链表l1和l2的节点个数分别为M和N，则时间复杂度O(max(M,N)), 附加空间复杂度O(max(M,N))
        :param l1:
        :param l2:
        :return:
        '''
        carry = 0  # 进位标志位
        head = ListNode(0)  # 哨兵结点
        res = head
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            s = carry + x + y
            res.next = ListNode(s%10)
            res = res.next
            # carry = s//10  # 取整效率低于减法
            carry = 1 if s >= 10 else 0
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        # 最后有进位的话，再添加一位
        if carry == 1:
            res.next = ListNode(1)
        return head.next
