"""
leetcode 347 求数组的前k的高频元素
思路：先使用字典统计数组元素(O(n))，然后构造一个大小为k的小顶堆，遍历字典即可(O(nlogk))。
"""
from typing import List
from collections import Counter
from heapq import *
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num2fre = {}
        for num in nums:
            if num in num2fre:
                num2fre[num] += 1
            else:
                num2fre[num] = 1
        num_set = list(num2fre.items())
        # for key, value in num2fre.items():
        #     num_set.append([key, value])

        minheap = []
        for item in num_set[:k]:
            heappush(minheap, (item[1], item[0]))
        for item in num_set[k:]:
            if item[1] > minheap[0][0]:
                heappop(minheap)
                heappush(minheap, (item[1], item[0]))

        ans = []
        for pair in minheap:
            ans.append(pair[1])
        return ans[::-1]

    def _topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        借助Counter容器实现
        :param nums:
        :param k:
        :return:
        """
        counter = Counter(nums)
        return [pair[0] for pair in counter.most_common(k)]


obj = Solution()
nums = [1,1,1,2,2,3]
k = 2
print(obj.topKFrequent(nums, k))