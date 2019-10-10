'''
leetcode 083 删除排序链表的重复元素
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次
思路：遍历链表，使用双指针prev和curr指向前一个结点和当前结点，判断是否相等，涉及链表中结点的删除操作。时间复杂度O(n)，空间复杂度O(1)
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 空链表或单个元素
        if not head or not head.next:
            return head
        # 两个及以上元素
        prev = head
        curr = head.next
        while curr:
            if prev.val == curr.val:
                prev.next = prev.next.next
                curr = curr.next
            else:
                prev = prev.next
                curr = curr.next
        return head