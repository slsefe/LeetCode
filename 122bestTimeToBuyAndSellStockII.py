"""
leetcode 122 买卖股票的最佳时机II
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票），但是不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
思路:遍历股票价格数组,判断每连续两天股票价格变化趋势,若价格升高则将其加到收益中。时间复杂度O(n),附加空间复杂度O(1)。
"""
from typing import List
class Solution:
    def max_profit(self, prices):
        """
        找到每次买卖时机（波谷和波峰）
        :param prices:
        :return:
        """
        i = 0
        profit = 0
        while i < len(prices)-1:
            while i < len(prices)-1 and prices[i+1] <= prices[i]:
                i += 1
            valley = prices[i]
            while i < len(prices)-1 and prices[i+1] >= prices[i]:
                i += 1
            peak = i
            profit += peak - valley
        return profit

    def _max_profit(self, prices: List[int]) -> int:
        """
        若相邻两天价格升高，将其加到收益中，是一种取巧的做法。
        :param prices:
        :return:
        """
        max_profit = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                max_profit += prices[i+1] - prices[i]
        return max_profit
