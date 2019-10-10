'''
leetcode 141 检测链表中是否有环
解法1：使用集合（哈希表）存储遍历到的结点内存地址，遍历链表，判断是否右重复结点。时间复杂度O(n)，空间复杂度O(n)。
解法2：快慢指针法，遍历链表，当快指针能够追上慢指针时，说明链表中有环，否则无环。时间复杂度O(n)，空间复杂度O(1)。

'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def hasCycle_v1(self, head: ListNode) -> bool:
        '''使用哈希表存储已经访问过的结点地址'''
        if not head or not head.next:
            return False
        id_set = set()
        while head:
            if id(head) in id_set:
                return True
            else:
                id_set.add(id(head))
            head = head.next
        return False

    def hasCycle_v2(self, head: ListNode) -> bool:
        '''快慢指针法'''
        if not head or not head.next:
            return False
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False