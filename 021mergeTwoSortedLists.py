'''
leetcode 21 合并两个有序链表
将两个有序链表合并为一个新的有序链表并返回
解法：
1.迭代：新建一个头指针，维护一个临时指针，遍历l1和l2，指针指向较小的值。当l1和l2其中一个为空时停止遍历，将临时指针指向非空链表，最后返回头指针的下一个节点。时间复杂度O(m+n), m,n分别是有序链表l1和l2的长度,附加空间复杂度O(m+n)。
2.递归：将l1和l2的合并操作分解为l1.next和l2的合并操作。递推公式：l1.next = merge(l1.next, l2), return l1。终止条件：l1或l2为空。时间复杂度O(m+n),m,n分别是有序链表l1和l2的长度, 附加空间复杂度O(n+m)。
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists_v1(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''迭代遍历'''
        dummy = ListNode(-1)  # 头结点
        l3 = dummy  # 新链表
        while l1 and l2:
            if l1.val <= l2.val:
                l3.next = ListNode(l1.val)
                l1 = l1.next
            else:
                l3.next = ListNode(l2.val)
                l2 = l2.next
            l3 = l3.next
        if l1:
            l3.next = l1
        elif l2:
            l3.next = l2
        return dummy.next

    def mergeTwoLists_v2(self, l1: ListNode, l2: ListNode) -> ListNode:
        """递归"""
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists_v2(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists_v2(l1, l2.next)
            return l2


def testSolution():
    l1 = ListNode(1)
    l1.next = ListNode(3)
    l1.next.next = ListNode(5)
    l2 = ListNode(2)
    l2.next = ListNode(4)
    l2.next.next = ListNode(6)
    solu = Solution()
    res = solu.mergeTwoLists_v1(l1, l2)
    assert res.val == 1
    assert res.next.val == 2
    assert res.next.next.val == 3
    assert res.next.next.next.val == 4
    assert res.next.next.next.next.val == 5
    assert res.next.next.next.next.next.val == 6
    assert res.next.next.next.next.next.next == None

    res = solu.mergeTwoLists_v2(l1, l2)
    assert res.val == 1
    assert res.next.val == 2
    assert res.next.next.val == 3
    assert res.next.next.next.val == 4
    assert res.next.next.next.next.val == 5
    assert res.next.next.next.next.next.val == 6
    assert res.next.next.next.next.next.next == None


if __name__ == '__main__':
    testSolution()

