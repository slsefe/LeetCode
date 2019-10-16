"""
leetcode 136 只出现一次的数字

给定一个非空的整数数组，只有一个元素出现一次，其他元素都出现两次，找到这个只出现一次的元素。

思路1：使用哈希表遍历给定数组，当前值在哈希表中存在时pop，不存在时添加，最后哈希表中剩余的唯一元素就是结果。时间复杂度O(N)，空间复杂度O(N)。

思路2：位运算。a^0=a, a^a=0, a^b^a = a^a^b。对数组中所有元素进行位运算，最后的结果就是出现次数为奇数（在这里为一次）的元素。时间复杂度O(N)，空间复杂度O(1)。
"""
from typing import List


class Solution:
    def singleNumber_v1(self, nums: List[int]) -> int:
        # 哈希表，时间复杂度O（N），空间复杂度O(N).
        d = dict()
        for num in nums:
            if num in d:
                d.pop(num)
            else:
                d[num] = 1
        return d.popitem()[0]

    def singleNumber_v2(self, nums: List[int]) -> int:
        # 位运算 异或
        # 0^a=a, a^a=0
        ans = 0
        for num in nums:
            ans = ans ^ num
        return ans
