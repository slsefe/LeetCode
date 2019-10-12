'''
leetcode 155 实现一个最小栈
设计一个支持push、pop、top操作，并能在常数时间内检索到最小元素的栈。
push(x)：x入栈；pop()：删除栈顶元素；top()：返回栈顶元素，getMin()：返回栈中的最小元素。
思路：使用两个栈实现。一个栈保存所有元素，另一个栈保存当前栈内的最小元素。
所有操作时间复杂度O(1), 附加空间复杂度O(N)。
'''


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []  # 保存
        self.mini_stack = []  # 保存元素

    def push(self, x: int) -> None:
        # 若最小栈为空或者x小于等于最小栈栈顶元素，同时入最小栈
        if not self.mini_stack or x <= self.mini_stack[-1]:
            self.mini_stack.append(x)
        self.stack.append(x)

    def pop(self) -> None:
        x = self.stack.pop()
        if x == self.mini_stack[-1]:
            self.mini_stack.pop()

    def top(self) -> int:
        if not self.stack:
            return None
        else:
            return self.stack[-1]

    def getMin(self) -> int:
        if not self.mini_stack:
            return None
        else:
            return self.mini_stack[-1]

def testMinStack():
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    assert obj.getMin() == -3
    obj.pop()
    assert obj.top() == 0
    assert obj.getMin() == -2


if __name__ == '__main__':
    testMinStack()