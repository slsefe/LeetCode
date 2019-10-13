'''
leetcode 009 回文数

判断一个整数是否为回文数。可以直接对整数进行反转，再判断是否相等。
'''


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 负数为非回文数
        if x < 0:
            return False
        # 对非负数进行翻转，若翻转后与原整数相等为回文数
        x_original = x
        x_reverse = 0
        while x != 0:
            x_reverse = 10 * x_reverse + x % 10
            x = x // 10
        return x_reverse == x_original


def testIsPalindrome():
    test_cases = [1221, 121, -121, 10, 100, 0]
    y = [True, True, False, False, False, True]
    solu = Solution()
    for i in range(len(test_cases)):
        assert solu.isPalindrome(test_cases[i]) == y[i]


if __name__ == '__main__':
    testIsPalindrome()
