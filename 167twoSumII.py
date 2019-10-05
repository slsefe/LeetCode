'''
leetcode 167 两数之和（二）
给定一个按照升序排列的有序数组，找到两个数使得他们之和等于目标值，返回这两个数的下标。
思路：双指针，时间复杂度O(n)，空间复杂度O(1)
'''
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 双指针，
        i, j = 0, len(numbers)-1
        while i < j:
            if numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                return [i+1, j+1]


if __name__ == '__main__':
    solu = Solution()
    nums_list = [
        [2,7,11,15],
        [1,5,5,8]
    ]
    target_list = [9,10]
    res_list = [
        [1,2],
        [2,3]
    ]
    for i in range(len(nums_list)):
        assert solu.twoSum(nums_list[i], target_list[i]) == res_list[i]