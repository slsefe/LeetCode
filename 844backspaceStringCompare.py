'''
leetcode 844 比较含退格的字符串

给定两个字符串S和T，字符串只含有a-z和#，其中#表示退格字符，判断两个字符串输入到编辑器之后是否相等。

思路：使用两个栈分别保存字符串的输出结果，比较即可。时间复杂度O(N)，空间复杂度O(N)。
'''


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        # 使用两个栈分别存储两个字符串
        stack1 = []
        stack2 = []
        for char in S:
            if char == '#' and stack1:  # 处理空栈时遇到的退格字符
                stack1.pop()
            elif 'a' <= char <= 'z':
                stack1.append(char)
        for char in T:
            if char == '#' and stack2:
                stack2.pop()
            elif 'a' <= char <= 'z':
                stack2.append(char)
        return stack1 == stack2


def test():
    solu = Solution()
    test_cases = [
        ["ab#c", "ad#c", True],
        ["ab##", "c#d#", True],
        ["a##c", "#a#c", True],
        ["a#c", "b", False]
    ]
    for test_case in test_cases:
        assert solu.backspaceCompare(test_case[0], test_case[1]) == test_case[2]


if __name__ == '__main__':
    test()
