'''
leetcode 232 使用栈实现队列

使用Python的列表模拟栈来实现队列，包括入队enqueue（在队尾插入一个元素），出队dequeue（删除并返回队头元素），获取队头元素peek，判断队列是否为空empty。

思路：使用两个栈来实现。新元素入队列时直接入栈1，时间复杂度O(1)。出队列时需要删除并获取栈1的栈底元素，于是将栈1的元素全部出栈并按顺序入栈2，这时栈2的栈顶元素为原来栈1的栈底元素，将栈2栈顶元素出栈即可。假设每次从栈1搬移N个元素到栈2，时间复杂度为O(n)，这N个元素出队列时的时间复杂度为O(1)，采取摊还分析则出队列时间复杂度为O(1)。获取队头元素，直接返回栈1的栈底元素即可，时间复杂度O(1)。由于队列中的数据一部分存在栈1，一部分存在栈2，当且仅当栈2为空且要删除队头元素时，将当前栈1所有元素搬移到栈2，故当栈1和栈2都为空时队列为空，时间复杂度O(1)。
'''
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 使用两个栈实现
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        # 若stack2为空，将stack1元素push到stack2并pop，否则直接pop
        if self.empty():
            return None
        elif not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
        else:
            return self.stack2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.empty():
            return None
        elif self.stack1:
            return self.stack1[0]
        else:
            return self.stack2[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if not self.stack1 and not self.stack2:
            return True
        else:
            return False

# Your MyQueue object will be instantiated and called as such:
def testMyStack():
    obj = MyQueue()
    assert obj.empty() == True
    obj.push(1)
    assert obj.empty() == False
    obj.push(2)
    assert obj.peek() == 1
    assert obj.pop() == 1
    assert obj.peek() == 2
    assert obj.pop() == 2
    assert obj.empty() == True


if __name__ == '__main__':
    testMyStack()
