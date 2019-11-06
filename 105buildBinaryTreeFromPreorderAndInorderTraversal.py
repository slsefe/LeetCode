"""
leetcode 105 从前序遍历和中序遍历构造二叉树
前序遍历+中序遍历构造二叉树。
思路：前序遍历为：根节点->左子树->右子树；中序遍历为：左子树->根节点->右子树，使用递归完成。
"""

from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        x = preorder[0]
        node = TreeNode(x)
        i = inorder.index(x)

        node.left = self.buildTree(preorder[1:i + 1], inorder[:i])
        node.right = self.buildTree(preorder[i + 1:], inorder[i + 1:])
        return node
