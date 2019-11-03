"""
leetcode 152 最大子数组积
给定一个整数数组nums，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。
类似题目：leetcode 53 最大子数组和
思路：和变为积，考虑序列中出现的负数和零这两种特殊情况。保留数组中的最大和最小子序列积，当遇到负数时，进行交换，ans变量保存目前的最大子序列积。
时间复杂度O(n),附加空间复杂度O(1),运行时间64ms, 内存消耗13.4MB.
"""


from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res, _max, _min = float('-inf'), 1, 1 
        for num in nums:
            if num < 0:
                _max, _min = _min, _max
            # 下面两行相当于最大子数组和中的sum=max(sum,0)
            # 当当前值num大于_max或小于_min时，抛弃前面序列，重置_max或_min
            _max = max(num, num*_max)
            _min = min(num, num*_min)
            # 相当于最大子数组和贪心解法中的res=max(res, sum)
            res = max(res, _max)
        return res
