'''
leetcode 029 两个整数相除
给定两个整数，范围为[-2147483648,2147483647]，实现两个整数相除运算，返回商。要求不使用除法、乘法、mod运算符。当结果溢出时，返回2^31-1。
思路：
1. 使用减法模拟除法：用被除数减去除数，记录次数
2. 使用位运算模拟除法，左移一位相当于乘以2，右移一位相当于除以2。
'''
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # 被除数为0的情况
        if dividend == 0:
            return 0
        # 被除数为-2147483648的情况
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        # 判断被除数和除数符号
        if (dividend ^ divisor) < 0:
            nega = True
        else:
            nega = False
        # 将被除数和除数变为正数进行移位
        t = dividend if dividend > 0 else -dividend
        d = divisor if divisor > 0 else -divisor
        # 找出2^n，使得被除数/2^n>除数
        res = 0
        for i in range(31, -1, -1):
            if (t>>i) >= d:
                res += 1<<i  # 商加上2^i
                t -= d<<i  # 被除数减去divisor*2^i
        return -res if nega else res