'''
leetcode 1021 删除括号字符串最外层的括号

给定一个只包含'('和')'的非空有效括号字符串，对其进行分解，得到多个非空有效括号字符串，删除每部分的最外层括号后返回。

思路：遍历给定的非空有效括号字符串，使用栈判断已遍历部分是否为非空有效括号字符串，当栈为空时，之前遍历的部分即为一个非空有效括号字符串，使用双指针记录每一部分的位置，删除最外层括号后添加到最后结果。时间复杂度O(N)，空间复杂度O(N)。
'''


class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        # 使用栈对原非空有效字符串进行分解，记录分解位置，删除首尾括号，进行拼接。
        stack = []
        ans = ''
        # 左括号入栈，右括号匹配则出栈，否则入栈。当栈空时记录下标。
        i, j = 0, 0
        for char in S:
            if char == '(':
                stack.append(char)
            elif char == ')' and stack[-1] == '(':
                stack.pop()
            j += 1
            # 栈为空时为一个非空有效括号字符串
            if not stack:
                ans += S[i + 1:j - 1]  # 删除首尾括号并拼接
                i = j
        return ans


def test():
    testcases = [
        ['(()())(())', '()()()'],
        ['(()())(())(()(()))', '()()()()(())'],
        ['()()', '']
    ]
    my_solution = Solution()
    for i in range(len(testcases)):
        assert my_solution.removeOuterParentheses(testcases[i][0]) == testcases[i][1]


if __name__ == '__main__':
    test()
