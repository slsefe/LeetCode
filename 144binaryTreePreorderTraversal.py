"""
leetcode 144 二叉树的前序遍历
方法一：递归
方法二：非递归，用栈保存结点
"""


from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorder_traversal_v1(self, root):
        """
        二叉树前序遍历的递归实现
        :param root:
        :return:
        """
        ans = []
        return self._preorder_traversal(root, ans)

    def _preorder_traversal(self, root, ans):
        """
        二叉树前序遍历递归实现的帮助函数
        :param root:
        :param ans:
        :return:
        """
        if not root:
            return []
        ans.append(root.val)
        if root.left:
            ans.append(root.left.val)
        if root.right:
            ans.append(root.right.val)
        return ans

    def preorderTraversal_v2(self, root: TreeNode) -> List[int]:
        """
        二叉树前序遍历的非递归实现
        :param root:
        :return:
        """
        if not root:
            return []
        stack, output = [], []
        stack.append(root)
        while stack:
            root = stack.pop()
            output.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
        return output
