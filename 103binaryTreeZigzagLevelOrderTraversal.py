"""
leetcode 103 二叉树的锯齿形层次遍历
二叉树的遍历分两种：深度优先遍历（前序、中序、后序）和广度优先遍历（层次遍历），其中深度优先遍历有递归实现和基于辅助栈的非递归实现，广度优先遍历是基于辅助队列实现的。
思路：与二叉树的层次遍历类似。
方法一：利用辅助队列，额外维护一个变量表示层数是否为偶数，当层数为偶数时，当前层遍历结果逆序。
方法二：利用辅助栈，额外维护一个表示层数的变量，当前层为奇数时，从右到左遍历当前层结点；当前层为偶数时，从左到右遍历当前结点。（与队列正好相反）
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        cur = [root]
        next = []
        flag = True
        ans = []
        while cur or next:
            level_ans = []
            for node in cur:
                level_ans.append(node.val)
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            if flag:
                ans.append(level_ans)
                flag = False
            else:
                ans.append(level_ans[::-1])
                flag = True
            cur = next
            next = []
        return ans