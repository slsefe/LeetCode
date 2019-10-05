'''
leetcode 31 下一个排列
给定使用数组存储的一个排列，返回下一个排列。若无下一个排列，返回最小的排列。
例子见测试用例

'''
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        j = len(nums) - 1
        # 找到第一个严格升序对
        while j > 0 and nums[j - 1] >= nums[j]:
            j -= 1
        # 不存在下一个更大的排列，需要单独处理
        if j != 0:
            # 在[j, len(nums)]区间找到大于nums[j]的最小元素，若存在多个相同的最小元素，与最后一个交换位置，确保交换之后此小区间仍然保持逆序。
            diff = 2147483647
            index = j
            for i in range(j, len(nums)):
                if 0 < nums[i] - nums[j-1] <= diff:
                    diff = nums[i] - nums[j-1]
                    index = i
            nums[j-1], nums[index] = nums[index], nums[j-1]
        # 对[j, len(nums)]区间，由逆序转换为正序
        m, n = j, len(nums)-1
        while m < n:
            nums[m], nums[n] = nums[n], nums[m]
            m += 1
            n -= 1
        return nums


if __name__ == '__main__':
    solu = Solution()
    assert solu.nextPermutation([1,2,3]) == [1,3,2]
    assert solu.nextPermutation([2,3,1]) == [3,1,2]
    assert solu.nextPermutation([3,2,1]) == [1,2,3]
    assert solu.nextPermutation([1,1,5]) == [1,5,1]
    assert solu.nextPermutation([2,3,1,3,3]) == [2,3,3,1,3]

