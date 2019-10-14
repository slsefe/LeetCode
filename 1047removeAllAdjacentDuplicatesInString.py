'''
leetcode 1047 删除字符串中相邻重复的字符

给定由小写字母组成的字符串，相邻重复字符删除会选择两个相邻且重复的字符并删除它们。在字符串上反复执行删除操作，知道无法继续删除，返回删除后的结果。

思路：使用栈来完成删除操作。遍历字符串，若栈不为空且当前字符与栈顶字符相同的栈顶字符出栈，否则当前字符入栈。遍历完成后将栈中的字符拼接起来即为删除后的结果。时间复杂度O(N)，空间复杂度为O(N)。
'''


class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for char in S:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        ans = ''
        for char in stack:
            ans += char
        return ans


def my_test():
    my_solution = Solution()
    testcases = [
        ['abbaca', 'ca'],
        ['abcddcba', '']
    ]
    for i in range(len(testcases)):
        assert my_solution.removeDuplicates(testcases[i][0]) == testcases[i][1]
