"""
leetcode 121 买卖股票的最佳时机1
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
例子：输入[7,1,5,3,6,1]，则最大收益为1，即第二天买入，第5天卖出。
思路：（1）二重循环，遍历所有情况，找出最大收益，时间复杂度O(n^2)，空间复杂度O(1)；
（2）动态规划解法：一重遍历，遍历过程中维护一个变量保存目前为止的最小股票价格和最大收益，时间复杂度O(n)，空间复杂度O(1)。
"""


from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 2147483647
        max_profit = 0
        for i in range(len(prices)):
            min_price = min(prices[i], min_price)
            max_profit = max(max_profit, prices[i] - min_price)
        return max_profit
