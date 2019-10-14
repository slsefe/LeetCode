"""
leetcode 150 逆波兰表达式求值

根据逆波兰表示法，求表达式的值。
"""
from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = set(list(['+', '-', '*', '/']))
        stack = []
        for token in tokens:
            if token in ops:
                num2 = stack.pop()
                num1 = stack.pop()
                if token == '+':
                    stack.append(num1 + num2)
                elif token == '-':
                    stack.append(num1 - num2)
                elif token == '*':
                    stack.append(num1 * num2)
                elif token == '/':
                    stack.append(int(num1 / num2))
            else:
                stack.append(int(token))
        return stack[-1]


def my_test():
    my_solution = Solution()
    testcases = [
        [["2", "1", "+", "3", "*"], 9],
        [["4", "13", "5", "/", "+"], 6],
        [["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22]
    ]
    for i in range(len(testcases)):
        assert my_solution.evalRPN(testcases[i][0]) == testcases[i][1]


if __name__ == '__main__':
    my_test()
