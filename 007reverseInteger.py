'''
leetcode 007 反转整数

给定一个32位的有符号整数，对其进行翻转。
'''


class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        is_positive = (x >= 0)
        x = abs(x)
        while x != 0:
            ans = 10 * ans + x % 10
            x = x // 10
        ans = ans if is_positive else -ans
        if ans > 2147483647 or ans < -2147483648:
            ans = 0
        return ans


def testReverse():
    solu = Solution()
    x_list = [123, -123, 120, -2147483648]
    res_list = [321, -321, 21, 0]
    for i in range(len(res_list)):
        assert solu.reverse(x_list[i]) == res_list[i]


if __name__ == "__main__":
    testReverse()
