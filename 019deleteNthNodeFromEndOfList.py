'''
leetcode 019 删除链表的倒数第N个节点
快慢指针法：慢指针指向头结点，快指针指向第n个节点。遍历链表，当快指针指向尾结点时，慢指针指向待删除节点的前一个结点，删除即可。时间复杂度O(N)，空间复杂度O(1)。
为了避免单元素链表删除后变为空链表无法访问的情况，设置哨兵结点。
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 双指针法：快指针在慢指针前面n个节点，当快指针到达尾结点时，慢指针到达待删除节点的前一个结点
        dummy = ListNode(-1)
        dummy.next = head
        slow, fast = dummy, dummy
        # 快指针在慢指针前面n个节点
        for _ in range(n):
            fast = fast.next
        # 找到待删除节点的前一个节点
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        # 删除slow指针指向的下一个节点
        slow.next = slow.next.next
        return dummy.next
