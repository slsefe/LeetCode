'''
leetcode 1: 两数之和
给定一个整数数组和一个目标值，在该数组中找到和为目标值的两个整数，返回它们的数组下标。数组中可能会有重复的元素，同一元素不能重复使用，每种输入只有一个正确答案。如给定`nums=[2,7,9,11], target=9`则返回`[0, 1]`。
'''
from typing import List

class Solution:
    def twoSum_v1(self, nums: List[int], target: int) -> List[int]:
        '''两重循环
        时间复杂度为O(n^2)，空间复杂度O(1)
        :param nums:
        :param target:
        :return:
        '''
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum_v2(self, nums: List[int], target: int) -> List[int]:
        '''利用哈希表，一次遍历

        这里把检测差值是否在字典中与把当前值添加到字典在同一个循环里实现，天然地避免了对同一元素重复考虑的问题。对于数组中的重复元素来说，若重复元素是要寻找的元素，则会返回，否则在字典中会只记录一次，因为已经验证过两个重复元素不是要返回的元素。

        时间复杂度O(n)，空间复杂度O(n)
        :param num:
        :param target:
        :return:
        '''
        d = dict()
        for i in range(len(nums)):
            if target-nums[i] in d:
                return [d[target-nums[i]], i]
            d[nums[i]] = i


def main():
    solu = Solution()
    nums_list = [
        [1, 7],
        [2, 3, 4],
    ]
    target_list = [8, 6]
    res_list = [
        [0, 1],
        [0, 2]
    ]
    for i in range(len(res_list)):
        assert solu.twoSum_v1(nums_list[i], target_list[i]) == res_list[i]
        assert solu.twoSum_v2(nums_list[i], target_list[i]) == res_list[i]
