'''
leetcode 234 回文链表
判断给定链表是否为回文链表
1.辅助数组+首尾指针：遍历链表，结点值保存在数组中，使用首尾指针判断数组元素是否为回文。时间复杂度O(n)，空间复杂度O(n)。
2.快慢指针+链表反转：快慢指针找到链表中间节点，对中间节点之后的结点进行翻转，判断两部分是否相同。时间复杂度O(n)，空间复杂度O(1)。
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome_v1(self, head: ListNode) -> bool:
        '''辅助列表法'''
        tmp = []
        while head:
            tmp.append(head.val)
            head = head.next
        left, right = 0, len(tmp)-1
        while left < right:
            if tmp[left] != tmp[right]:
                return False
            else:
                left += 1
                right -= 1
        return True

    def isPalindrome_v2(self, head: ListNode) -> bool:
        # 快慢指针找中间节点
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # 链表节点个数为奇数，fast指向尾节点，slow指向中间节点
        # 链表节点个数为偶数，fast指向空，slow指向右中位数结点
        # 翻转中间节点后边的链表节点
        prev = None
        while slow:
            curr = slow.next
            slow.next = prev
            prev = slow
            slow = curr
        # 比较两部分是否相同
        while head and prev:
            if head.val != prev.val:
                return False
            else:
                head = head.next
                prev = prev.next
        return True
