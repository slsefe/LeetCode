'''
leetcode 69 求给定一个非负整数的整数平方根
给定一个非负整数，求它的平方根，保留整数部分。
特殊情况考虑：
    - 输入为0时返回0
    - 输入为1、2、3时返回1
    - 输入为4-8时返回2
    - 输入特别大时，能否快速得出结果，避免O(n)复杂度
'''
import numpy as np
class Solution:
    def mySqrt_v1(self, x):
        '''
        二分法
        :param x:
        :return:
        '''
        # sqrt(x)取值范围为[0, x//2+1]
        left = 0
        right = x//2 + 1
        while left < right:
            mid = (left + right + 1) >> 1  # 右中位数
            if mid ** 2 > x:
                right = mid - 1
            else:
                left = mid
        return int(left)


    def mySqrt_v2(self, x):
        '''
        牛顿迭代法求方程的根
        :param x:
        :return:
        '''
        # sqrt(x)的上界
        y0 = x//2 + 1
        # 从上界开始比较
        while y0 ** 2 > x:
            y0 = (y0 + x/y0) /2
        return int(y0)


if __name__ == '__main__':
    solu = Solution()
    input_list = [0, 1, 3, 4, 8, 9, 1000000, 1000001, 100000000, 100000001]
    input_list.extend(np.random.randint(0, 2147483647, 10))
    print(input_list)
    res_list = list(map(int, np.sqrt(input_list)))
    for i in range(len(input_list)):
        assert solu.mySqrt_v1(input_list[i]) == res_list[i]
        assert solu.mySqrt_v2(input_list[i]) == res_list[i]