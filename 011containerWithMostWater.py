'''
leetcode 11 盛最多水的容器
给定一个数组，数组下标代表坐标轴的位置，元素值代表高度，找出可以盛最多水的容量。
如：给定height=[1,8,6,2,5,4,8,3,7]，结果为height[1]和height[8]组成的两条线可以容纳最多的水，即area=(8-1)*min(height[1], height[8])=49.
思路：
1. 两重循环，时间复杂度O(n^2),空间复杂度O(1)
2. 双指针，初始化为首尾指针，比较两个指针的元素大小，移动值较小的指针，若两个指针对应的元素值相等，则移动任意一个即可。从首尾向中间移动指针相当于减小容器长度，则必须增加容器高度，容器高度取决于两个指针的较小的元素值。
'''
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 暴力两重循环超时，双指针做法：值小的指针向内移动
        i = 0
        j = len(height)-1
        res = 0
        while i<j:
            h = min(height[i], height[j])
            res = max(res, h*(j-i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return res


if __name__ == '__main__':
    solu = Solution()
    height_list = [1,8,6,2,5,4,8,3,7]
    assert solu.maxArea(height_list) == 49