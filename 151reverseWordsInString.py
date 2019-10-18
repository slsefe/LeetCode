#!/usr/bin/python
"""
leetcode 151 翻转字符串中的单词

对于给定的字符串，翻转字符串中单词的位置，忽略字符串首尾的空格和单词之间的多余空格。

思路：首先去除首尾空格，按照空格切分，对切分结果逆序排列，去除中间的多余空格，按照空格进行拼接。时间复杂度O(N)，空间复杂度O(N)。
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        """
        翻转字符串中单词的位置，如"I am a student."翻转为"student. a am I"。
        :param str:
        :return:
        """
        res = ''
        # 处理首尾多余的空格字符，按照空格划分，并逆序
        for word in s.strip().split(' ')[::-1]:
            # 对单词之间的多余空格进行处理
            word = word.strip()
            if word:
                res += word
                res += ' '
        # 处理最后一次添加的空格
        return res.strip()


def my_test():
    my_solution = Solution()
    testcases = [
        ['I am a student.', 'student. a am I']
    ]
    for testcase in testcases:
        assert my_solution.reverseWords(testcase[0]) == testcase[1]


if __name__ == '__main__':
    my_test()
