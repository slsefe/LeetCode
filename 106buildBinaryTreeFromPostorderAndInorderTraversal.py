"""
leetcode 106 从中序遍历和后序遍历构造二叉树
中序遍历+后序遍历构造二叉树。
思路：后序遍历为：左子树->右子树->根节点；中序遍历为：左子树->根节点->右子树，使用递归完成。
"""

from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        x = postorder[-1]
        node = TreeNode(x)
        i = inorder.index(x)

        node.left = self.buildTree(inorder[:i], postorder[:i])
        node.right = self.buildTree(inorder[i+1:], postorder[i:-1])
        return node
