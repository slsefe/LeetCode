'''
leetcode 146 设计实现LRU缓存淘汰算法
思路：使用Python自带的有序字典OrderedDict实现。要求O(1)时间复杂度实现获取数据get(key)和写入数据put(key, value)方法。get(key)为从缓存中获取数据，若数据存在，返回key对应的值，否则返回-1。put(key, value)：若key在缓存中不存在则在缓存中写入，当缓存容量达到上限时，应该删除最近最少使用的数据。
'''
from collections import OrderedDict

class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        OrderedDict.__init__()
        self.capacity = capacity

    def get(self, key: int) -> int:
        # 若key不在字典中，返回-1；否则将key移到字典末尾并返回其值
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        # 若key在字典中，将其移到字典末尾并更新其值
        if key in self:
            self.move_to_end(key)
            self[key] = value
        else:  # 若key不在字典中，判断字典元素个数。若字典元素个数超过容量，删除字典头部元素，并将key添加到字典尾部；否则直接将key添加到字典尾部。
            if len(self) == self.capacity:
                self.popitem(last=False)
            self[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)