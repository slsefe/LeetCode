"""
leetcode 53 最大子数组和
给定一个整数数组nums，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
例子：输入数组[-2,1,-3,4,-1,2,1,-5,4]，输出连续子数组[4,-1,2,1]的和最大，为6。
1.暴力枚举，三重循环，时间复杂度O(n^3)，附加空间复杂度O(1)，运行时间超出限制。
2.优化枚举，二重循环，时间复杂度O(n^2)，附加空间复杂度O(1)，运行时间146ms, 内存消耗45.3MB。
3.贪心算法，一冲循环，时间复杂度O(n)，附加空间复杂度O(1)，运行时间52ms, 内存消耗13.4MB.
"""
from typing import List
class Solution:

    def maxSubArray_v1(self, nums: List[int]) -> int:
        """
        三重循环
        :param nums:
        :return:
        """
        ans = -2147483648
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                sum = 0
                for k in range(i, j+1):
                    sum += nums[k]
                ans = max(ans, sum)
        return ans

    def maxSubArray_v2(self, nums: List[int]) -> int:
        """
        二重循环
        :param nums:
        :return:
        """
        ans = -2147483648
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                ans = max(ans, sum)
        return ans

    def maxSubArray_v3(self, nums: List[int]) -> int:
        """
        贪心法
        :param nums:
        :return:
        """
        ans = -2147483648
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            ans = max(ans, sum)
            sum = max(sum, 0)
        return ans


def my_test():
    nums = list(map(int, input().strip().split(",")))
    my_solution = Solution()
    print(my_solution.maxSubArray_v1(nums))
    print(my_solution.maxSubArray_v2(nums))
    print(my_solution.maxSubArray_v3(nums))


if __name__ == '__main__':
    my_test()