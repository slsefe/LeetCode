'''
leetcode 496 下一个更大的元素I

给定两个没有重复元素的数组nums1和nums2，其中nums1是nums2的子集，找到nums1中的每个元素在nums2中的下一个比其大的值，如果不存在更大的值返回-1。

思路1：暴力法，两层循环。对于nums2中的每个元素找到下一个更大的值，保存在哈希表中，时间复杂度O(N)，空间复杂度O(N)。然后遍历nums1中的每个元素，在哈希表中找到对于的值，时间复杂度O(M)，空间复杂度O(M)。合计时间复杂度O(N)，空间复杂度O(N)。

思路2：维护一个递减栈
'''

from typing import List
class Solution:
    def nextGreaterElement_v1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 两次循环
        # 对于nums2中的每一个元素，计算其下一个更大的元素，保存在字典中
        mapping = dict()
        for i, num in enumerate(nums2):
            j = i + 1
            while j < len(nums2) and nums2[j] <= num:
                j += 1
            if j == len(nums2):
                mapping[num] = -1
            else:
                mapping[num] = nums2[j]

        res = []
        for num in nums1:
            res.append(mapping[num])
        return res


def testNextGreaterElement():
    obj = Solution()
    nums1_list = [
        [4, 1, 2],
        [2, 4]
    ]
    nums2_list = [
        [1, 3, 4, 2],
        [1, 2, 3, 4]
    ]
    res_list = [
        [-1, 3, -1],
        [3, -1]
    ]
    for i in range(len(res_list)):
        assert obj.nextGreaterElement_v1(nums1_list[i], nums2_list[i]) == res_list[i]


if __name__ == '__main__':
    testNextGreaterElement()