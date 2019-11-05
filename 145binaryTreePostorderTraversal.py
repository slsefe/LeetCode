"""
leetcode 145 二叉树的后序遍历
方法一：递归
方法二：非递归，借助前序遍历的非递归实现。前序遍历为：根节点->左子节点->右子结点，后序遍历为：左子节点->右子结点->根节点。若将前序遍历的左右子结点位置交易，则正好与后序遍历相反。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorder_traversal_v1(self, root):
        """
        二叉树后序遍历的递归实现
        :param root:
        :return:
        """
        if not root:
            return []
        ans = []
        return self._postorder_traversal(root, ans)

    def _postorder_traversal(self, root, ans):
        if root.left:
            self._postorder_traversal(root.left, ans)
        if root.right:
            self._postorder_traversal(root.right, ans)
        ans.append(root.val)
        return ans

    def postorder_traversal(self, root):
        if not root:
            return []
        stack = [root]
        ans = []
        while stack:
            root = stack.pop()
            ans.append(root.val)
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
        return ans[::-1]


