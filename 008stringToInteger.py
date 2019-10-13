'''
leetcode 008 字符串转换整数

实现一个atoi函数，能够将字符串转换为整数。
首先需要丢弃开头空格字符，找到第一个非空格字符。当第一个非空格字符为正号或负号时，将其与后面尽可能多的连续数字一起构成整数。当第一个非空格字符为数字时，直接将其与后面尽可能多的连续数字一起构成整数。当第一个非空格字符为其他字符时，返回0.
返回的数字应该在32位的有符号整数范围内，如果超过则返回允许范围内的最小值或最大值。
'''
class Solution:
    def myAtoi(self, str: str) -> int:
        # 空字符串返回0
        if str == '':
            return 0
        # 是否已经读取到合法输入
        is_begin = False
        # 正数or负数
        is_positive = True
        # 字符串下标
        index = 0
        # 结果
        res = 0
        while index < len(str):
            if not is_begin:
                if str[index] == ' ':
                    # 忽略起始的空格
                    index += 1
                elif str[index] == '+':
                    is_positive = True
                    is_begin = True
                    index += 1
                elif str[index] == '-':
                    is_positive = False
                    is_begin = True
                    index += 1
                elif str[index] >= '0' and str[index] <= '9':
                    is_begin = True
                    res = 10 * res + int(str[index])
                    index += 1
                else:
                    return 0
            else:
                if str[index] >= '0' and str[index] <= '9':
                    res = 10 * res + int(str[index])
                    index += 1
                else:
                    break
        # 对结果进行正负号判断和溢出判断
        res = res if is_positive else -res
        if res > 2147483647:
            return 2147483647
        elif res < -2147483648:
            return -2147483648
        else:
            return res


def testMyAtoi():
    inputs_list = [
        '  ',
        ' 42',
        ' +42',
        ' -42',
        ' +-',
        '2147483648 ',
        ' word22'
    ]
    output_list = [0, 42, 42, -42, 0, 2147483647, 0]
    obj = Solution()
    for i in range(len(inputs_list)):
        assert obj.myAtoi(inputs_list[i]) == output_list[i]


if __name__ == '__main__':
    testMyAtoi()
