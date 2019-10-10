'''
leetcode 707 设计链表
可以设计单链表或双向链表，单链表每个节点应该包括val和next，双向链表还应包括prev，下标index从0开始。
实现以下功能：
get(index)：当index合法时获取链表第index个结点的值，否则返回-1。
addAtHead(val)：在链表的第一个节点之前插入一个值为val的结点。插入后，新结点将成为链表的第一个节点。
addAtTail(val)：在链表的最后一个结点之后插入一个值为val的结点。插入后，新节点将成为链表的最后一个结点。
addAtIndex(index, val)：在链表的第index个节点之前插入一个值为val的结点。如果index小于0，在头部插入节点；如果index等于链表长度，在尾部插入节点；如果index大于链表长度，不插入。
deleteAtIndex(index)：如果index有效，删除链表的第index个结点
'''


class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 头节点
        self.head = Node(-1)
        self.num = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.num:
            return -1
        p = self.head
        for i in range(index + 1):
            p = p.next
        return p.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        p = Node(val)
        p.next = self.head.next
        self.head.next = p
        self.num += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        p = self.head
        for i in range(self.num):
            p = p.next
        q = Node(val)
        p.next = q
        self.num += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < 0:  # 小于0在头部插入
            self.addAtHead(val)
        elif index == self.num:  # 等于链表长度在尾部插入
            self.addAtTail(val)
        elif index > self.num:  # 大于链表长度不插入
            return
        else:  # 否则在第index个节点之前插入
            p = self.head
            # 找到第i-1个节点
            for i in range(index):
                p = p.next
            q = Node(val)
            q.next = p.next
            p.next = q
            self.num += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.num:
            return
        else:
            p = self.head
            for i in range(index):
                p = p.next
            p.next = p.next.next
            self.num -= 1

# Your MyLinkedList object will be instantiated and called as such:
def testMyLinkedList():
    obj = MyLinkedList()
    obj.addAtHead(1)
    assert obj.get(0) == 1
    assert obj.get(1) == -1
    obj.addAtTail(3)
    assert obj.get(0) == 1
    assert obj.get(1) == 3
    assert obj.get(2) == -1
    obj.addAtIndex(1,2)
    assert obj.get(0) == 1
    assert obj.get(1) == 2
    assert obj.get(2) == 3
    obj.deleteAtIndex(1)
    assert obj.get(0) == 1
    assert obj.get(1) == 3
    assert obj.get(2) == -1


if __name__ == '__main__':
    testMyLinkedList()