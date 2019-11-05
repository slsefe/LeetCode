"""
leetcode 102 二叉树的层次遍历
二叉树的遍历分两种：深度优先遍历（前序、中序、后序）和广度优先遍历（层次遍历），其中深度优先遍历有递归实现和基于辅助栈的非递归实现，广度优先遍历是基于辅助队列实现的。
思路：基于两个队列实现，第一个队列保存当前层的结点（初始化为根节点），第二个队列保存当前层的子结点（初始化为空）。首先遍历当前根节点，遍历当前层的结点，并将其子结点（若存在）入下一层子结点队列，当前层结点遍历完成后，将下一层结点队列赋值为当前层队列，下一层结点队列清空，直到下一层结点队列为空。
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        cur = [root]
        next = []
        ans = []
        while cur or next:
            level_ans = []
            for node in cur:
                level_ans.append(node.val)
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            cur = next
            next = []
            ans.append(level_ans)
        return ans
