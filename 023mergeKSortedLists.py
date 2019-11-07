"""
leetcode 023 合并k个有序链表
这道题有很多种解决方法：（n为所有链表的节点个数，k为有序链表个数）
（1）将k个链表的结点值都添加到一个数组中，排序后构造链表，时间复杂度O(nlogn)，空间复杂度O(n)
（2）逐一比较k个节点，时间复杂度为O(kn)，空间复杂度为O(n)
（3）借助21题（合并两个有序链表），进行k-1次两个有序链表的合并，时间复杂度O(kn)，空间复杂度O(1)
（4）维护一个容量为k的小顶堆优先级队列，n次堆化，时间复杂度为O(nlogk)，空间复杂度为O(n+k)
（5）分治法：没两个进行合并，时间复杂度为O(nlogk)，空间复杂度为O(1)
"""
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = dummy = ListNode(-1)
        # 构建一个容量为k的小顶堆优先队列（这里下标从0开始）
        heap = [list for list in lists if list]
        n = len(heap)
        for i in range(n // 2 - 1, -1, -1):
            self._heapfy(heap, n, i)

        while heap:
            # 出堆
            node = ListNode(heap[0].val)
            dummy.next = node
            dummy = node
            # 入堆
            if heap[0].next:
                heap[0] = heap[0].next
            else:
                heap[0] = heap[-1]
                heap.pop()
                n -= 1
            # 堆化
            self._heapfy(heap, n, 0)
        return head.next

    def _heapfy(self, heap, n, i):
        """对heap的第i个节点从上往下进行堆化"""
        while True:
            min_pos = i
            if 2 * i + 1 <= n - 1 and heap[2 * i + 1].val < heap[i].val:
                min_pos = 2 * i + 1
            if 2 * (i + 1) <= n - 1 and heap[2 * i + 2].val < heap[min_pos].val:
                min_pos = 2 * (i + 1)
            if min_pos == i:
                break
            heap[i], heap[min_pos] = heap[min_pos], heap[i]
            i = min_pos