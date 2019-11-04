"""
leetcode 128 最长连续序列
给定一个未排序的数组，要求返回最长连续序列的长度，要求时间复杂度O(n)。。
例子：给定[100,4,1,200,3,2],最长连续序列为[1,2,3,4],返回4。
思路：因为要求时间复杂度为O(n)，不能排序。首先使用哈希表对数组去重，然后遍历哈希表，找到所有可能序列的第一个元素（其前一个元素不在字典中），计算以当前元素为头的连续序列长度。
"""
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_length = 0
        for num in nums_set:
            if num-1 not in nums_set:
                cur_num = num
                cur_length = 1
                while cur_num+1 in nums_set:
                    cur_length += 1
                    cur_num += 1
                max_length = max(max_length, cur_length)
        return max_length


def my_test():
    my_solution = Solution()
    while True:
        nums = list(map(int, input().strip().split(",")))
        print(my_solution.longestConsecutive(nums))


if __name__ == "__main__":
    my_test()