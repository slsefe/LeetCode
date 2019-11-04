"""
leetcode 394 字符串解码
给定一个字符串，包括0-9，a-z,A-Z,[,]，其中数字表示后面[]中的字符串重复的次数，注意[]中只含有字母，而[]可以嵌套。
例子：3[a]2[bc], 3[a2[bc]], 2[abc]3[cd]ef
思路：类似于表达式计算，使用栈实现。维护一个数字栈和一个字符串栈，在维护一个当前数字和当前字符串，遇到数字时更新数字，遇到字符串时更新字符串，遇到[时当前数字和当前字符串分别入栈，当前数字和字符串重置；遇到]时当前数字必为0，当前字符串必不为空，数字栈出栈，当前字符串重复一定次数，字符串栈顶字符出栈，与当前字符串拼接，赋值为当前字符串。最后返回当前字符串。时间复杂度O(n)，空间复杂度O(n)。
"""


class Solution:
    def decodeString(self, s: str) -> str:
        num_stack, str_stack = [], []
        num, cur = 0, ''
        for char in s:
            if '0' <= char <= '9':
                num = 10*num + int(char)
            elif 'a' <= char <= 'z' or 'A' <= char <= 'Z':
                cur += char
            elif char == '[':
                num_stack.append(num)
                num = 0
                str_stack.append(cur)
                cur = ''
            elif char == ']':
                str_stack[-1] += num_stack.pop() * cur
                cur = str_stack.pop()
        return cur
