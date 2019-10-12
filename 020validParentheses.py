'''
leetcode 20 有效的括号
给定一个只包含(){}[]6种字符的字符串，判断括号是否有效。
思路：属于栈的典型应用之一，使用Python的列表模拟栈来实现。使用字典保存括号的匹配关系，遍历字符串，遇到右括号就与栈顶元素比较，遇到左括号就入栈。括号匹配且匹配完成栈为空则整体匹配成功，否则匹配失败。
'''
class Solution:
    def isValid(self, s: str) -> bool:
        # 使用数组模拟栈
        stack = []
        # 使用hash表存储匹配关系
        mapping = {")":"(", "}":"{", "]":"["}
        # 对字符串中的每个字符进行匹配，左括号入栈，右括号与栈顶元素匹配，匹配成功栈顶元素出栈，否则失败。
        for char in s:
            if char in mapping:
                # 若栈非空获取栈顶元素（这里栈顶元素已经出栈）
                if stack:
                    elem = stack.pop()
                else:
                    return False  # 出现栈底元素为右括号匹配失败

                # 不匹配返回失败
                if mapping[char] != elem:
                    return False

            else:  # 假设输入都为合法字符，左括号入栈
                stack.append(char)
        # 匹配完成，若栈非空匹配失败，否则匹配成功
        if stack:
            return False
        else:  # 匹配完成栈不为空匹配失败
            return True


def testIsValid():
    solu1 = Solution()
    test_str = [
        '',
        ')',
        '()',
        '(]',
        '(][)',
        '()[]{}',
        '([{}])',
        '[{{()}}]'
    ]
    test_res = [True, False, True, False, False, True, True, True]
    for i in range(len(test_str)):
        assert solu1.isValid(test_str[i]) == test_res[i]


if __name__ == '__main__':
    testIsValid()
