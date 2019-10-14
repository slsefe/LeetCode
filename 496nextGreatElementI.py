"""
leetcode 496 下一个更大的元素I

给定两个没有重复元素的数组nums1和nums2，其中nums1是nums2的子集，找到nums1中的每个元素在nums2中的下一个比其大的值，如果不存在更大的值返回-1。

思路1：暴力法，两层循环。对于nums2中的每个元素找到下一个更大的值，保存在哈希表中，最好时间复杂度O(N)，最坏时间复杂度O(N^2)，平均时间复杂度O(N^2)，空间复杂度O(N)。然后遍历nums1中的每个元素，在哈希表中找到对应的值，时间复杂度O(M)，空间复杂度O(M)。合计时间复杂度O(N^2)，空间复杂度O(N)。

思路2：维护一个递减栈，使用哈希表保存nums2中每个元素的下一个更大值。首先遍历nums2元素并依次入栈，若栈不为空且当前元素大于栈顶元素，则栈顶元素出栈，将当前元素置为栈顶元素的下一个更大元素，当前元素入栈。遍历nums1，在哈希表中寻找对应的value，若不存在说明无下一个更大的元素返回-1。时间复杂度O(N)，空间复杂度O(N)。
"""
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

    def nextGreaterElement_v2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 维护一个递减栈，使用哈希表记录更新每个元素的下一个更大元素
        stack = []
        d = dict()
        for num in nums2:
            while stack and num > stack[-1]:
                d[stack.pop()] = num
            stack.append(num)
        ans = []
        for num in nums1:
            if num in d:
                ans.append(d[num])
            else:
                ans.append(-1)
        return ans


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
        assert obj.nextGreaterElement_v2(nums1_list[i], nums2_list[i]) == res_list[i]


if __name__ == '__main__':
    testNextGreaterElement()
