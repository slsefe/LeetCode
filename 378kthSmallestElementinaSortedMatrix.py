"""
leetcode 378 排序矩阵中的第k小元素
题目：给定一个nxn的排序矩阵，每行从小到大，每列从小到大，找出这个矩阵中的第k小元素。
方法1：二分查找
方法2：基于大顶堆的优先级队列。输出多个有序列表中的第k小元素。首先维护一个大小为min(k,n)的小顶堆，然后进行k次出堆和入堆操作。堆顶元素出堆后，若当前行还有剩余元素，入堆，否则没有元素入堆。第k个出堆的元素即为第k小元素。建堆的时间复杂度为O(min(k,n)),k次堆化的时间复杂度为O(k*log(min(k,n)))，总的时间复杂度为O(min(k,n)+k*log(min(k,n)))
注意：一般来说求k大元素使用小顶堆，求k小元素使用大顶堆。但是此题中数组已经有序，使用大顶堆的话，需要遍历矩阵所有元素，最后堆顶元素即为第k小元素，时间复杂度为O(K)+O(n^2*logk).
"""
from heapq import heappush, heappop
from typing import List
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # 维护一个容量为min(k,n)的小顶堆，第k次出堆的元素即为第k小元素
        n = len(matrix)
        minheap = []
        # min(k,n)个元素入堆并堆化，时间复杂度为O(min(k,n))
        for i in range(min(n, k)):
            heappush(minheap, (matrix[i][0], i, 0))
        # k个元素出堆，k个元素入堆并堆化，时间复杂度O(k*log(min(k,n)))
        account = 0
        while account < k:
            account += 1
            x, i, j = heappop(minheap)
            if j < n-1:
                heappush(minheap, (matrix[i][j+1], i, j+1))
        return x
