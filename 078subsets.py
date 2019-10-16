"""
leetcode 078 子集

给定一个不包含重复元素的整数数组，返回这个数组元素可能构成的所有集合。如给定nums=[1,2,3]，应当返回[[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]。

思路1：使用库函数itertools.combination()得到所有的组合情况。
思路2：迭代法。数组长度增加1，结果数组增加一倍。res+=[nums[i] + num for num in res]
思路3：位运算。
"""
from typing import List
from itertools import combinations


class Solution:
    def solution1(self, nums: List[int]) -> List[List[int]]:
        """组合数库函数"""
        res = []
        for i in range(len(nums)+1):
            for num in combinations(nums, i):
                res.append(num)
        return res

    def solution2(self, nums: List[int]) -> List[List[int]]:
        """迭代法："""
        ans = [[]]
        for i in range(len(nums)):
            ans += [[nums[i]] + num for num in ans]
        return ans
