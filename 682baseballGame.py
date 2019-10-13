'''
leetcode 682 棒球比赛

给定一个字符串列表，每个字符串可以是以下四种类型之一：
1.整数（一轮的得分）：直接表示您在本轮中获得的积分数。
2. "+"（一轮的得分）：表示本轮获得的得分是前两轮有效回合得分的总和。
3. "D"（一轮的得分）：表示本轮获得的得分是前一轮有效回合得分的两倍。
4. "C"（一个操作，这不是一个回合的分数）：表示最后一个有效回合的分数是无效的，应该被移除。
返回所有回合中得分的总和。

思路：使用栈来保存每一轮获得的分数，遇到整数、"+"、"D"则计算相应得分并入栈，遇到"C"则栈顶元素出栈，最后返回栈内元素的和。时间复杂度O(N)，空间复杂度O(N)。
'''


from typing import List
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        # 使用栈存放每一轮的分值
        stack = []
        for op in ops:
            if op == 'C':
                stack.pop()
            elif op == 'D':
                stack.append(2*stack[-1])
            elif op == '+':
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(op))
        return sum(stack)


def testCalPoints():
    test_inputs = [
        ["5", "2", "C", "D", "+"],
        ["5","-2","4","C","D","9","+","+"]
    ]
    expected_points = [30, 27]
    solu = Solution()
    for i in range(len(test_inputs)):
        assert solu.calPoints(test_inputs[i]) == expected_points[i]


if __name__ == '__main__':
    testCalPoints()
