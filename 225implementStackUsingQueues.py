'''
leetcode 225 使用队列实现栈的下列操作：

push(x)：元素x入栈；
pop()：移除并返回栈顶元素；
top()：获取栈顶元素；
empty()：返回栈是否为空

思路：使用Python容器类collections的deque（双端队列）来模拟一个队列实现栈。deque具有在两端进行添加、移除元素的函数。
'''

import collections
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = collections.deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q.appendleft(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """ 
        return self.q[0]
        
    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not len(self.q)


def test_my_stack():
    # Your MyStack object will be instantiated and called as such:
    obj = MyStack()
    assert obj.empty() == True
    obj.push(1)
    assert obj.empty() == False
    assert obj.top() == 1
    obj.pop()
    assert obj.empty() == True
    obj.push(2)
    obj.push(3)
    assert obj.top() == 3
    assert obj.pop()
    assert obj.top() == 2


if __name__ == '__main__':
    test_my_stack()
