"""
leetcode 215 求无序数组中的第k大元素
方法1：先排序，再按下标寻找，时间复杂度为O(nlogn)
方法2：维护一个容量为k的小顶堆，将数组中元素依次插入，最后堆顶元素即为第k大元素。时间复杂度为O(nlogk)，空间复杂度为O(k)
方法3：借助快速排序的思想，
"""
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 维护一个容量为k的小顶堆，若当前元素大于堆顶元素，则替换堆顶元素，并进行堆化，遍历数组。
        heap = nums[:k]
        for i in range(k // 2 - 1, -1, -1):
            self._heapfy(heap, k, i)
        for j in range(k, len(nums)):
            if nums[j] > heap[0]:
                heap[0] = nums[j]
                self._heapfy(heap, k, 0)
        return heap[0]

    def _heapfy(self, heap, k, i):
        """
        从上往下堆化第i个元素，时间复杂度为O(logk)
        :param heap:
        :param k:
        :param i:
        :return:
        """
        while True:
            min_pos = i
            if 2 * i + 1 < k and heap[i] > heap[2 * i + 1]:
                min_pos = 2 * i + 1
            if 2 * i + 2 < k and heap[min_pos] > heap[2 * i + 2]:
                min_pos = 2 * i + 2
            if i == min_pos:
                break
            heap[i], heap[min_pos] = heap[min_pos], heap[i]
            i = min_pos

