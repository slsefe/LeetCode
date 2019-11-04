"""
leetcode 611 数组中有效三角形的个数
题目描述：给定一个整数数组，判断数组中的元素能够组成多少个三角形。
分析：三角形三边条件：任意两边之和大于第三边->较小边之和大于最大边。
思路：首先对数组元素进行排序，然后固定最大边（从大到小遍历），利用首尾指针判断是否为有效三角形，注意判断过程中需要去冗余。时间复杂度O(n^2)，空间复杂度O(1)。
"""
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        num = 0
        for i in range(len(nums)-1, 1, -1):
            left, right = 0, i-1
            while left < right:
                # 若left, right, i构成三角形，则{left, right-1}, right和i构成三角形，去冗余
                if nums[left] + nums[right] > nums[i]:
                    num += (right-1) - left + 1
                    right -= 1
                else:
                    left += 1
        return num