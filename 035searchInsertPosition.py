'''
LeetCode 35 搜索目标值在数组中的插入位置
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
你可以假设数组中无重复元素。

- 考虑以下几种情况：
    - 空数组时返回0
    - 数组中只含有单个元素的情况，目标值小于等于数组元素时返回0，大于数组元素时返回1
    - 目标值存在于数组中时，返回其下标
    - 目标值不存在于数组中，返回前一元素下标+1
    - 目标值应该插入到数组头部时，返回0
    - 目标值应该插入到数组尾部，返回数组长度n
'''
class Solution:
    def searchInsert_v1(self, nums, target):
        '''
        单指针一次遍历，时间复杂度O(N), 附加空间复杂度O(1)
        :param nums:
        :param target:
        :return:
        '''
        i = 0
        while (i < len(nums) and nums[i] < target):
            i += 1
        return i


    def searchInsert_v2(self, nums, target):
        '''
        二分查找
        :param num:
        :param target:
        :return:
        '''
        # 二分查找
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if nums[left] < target:
            left += 1
        return left

if __name__ == '__main__':
    solu = Solution()
    nums_list = [
        [1],
        [1],
        [1],
        [1, 3, 5, 6],
        [1, 3, 5, 6],
        [1, 3, 5, 6],
        [1, 3, 5, 6]
    ]
    targets_list = [0, 1, 2, 0, 3, 4, 7]
    res_list = [0, 0, 1, 0, 1, 2, 4]
    for i in range(len(res_list)):
        assert solu.searchInsert_v1(nums_list[i], targets_list[i]) == res_list[i]
        assert solu.searchInsert_v2(nums_list[i], targets_list[i]) == res_list[i]