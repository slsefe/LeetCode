"""
leetcode 94 二叉树的中序遍历
方法一：递归实现
方法二：非递归实现。思路：使用栈来保存需要访问的结点，使用root指针来表示当前访问节点，使用ans来保存当前结点的值。（1）根节点及其左子节点入栈；（2）从无左子节点的结点开始，遍历此节点，再遍历其右子结点。
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorder_traversal_v1(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ans = []
        return self._inorder_traversal(root, ans)

    def _inorder_traversal(self, root, ans):
        if root.left:
            self._inorder_traversal(root.left, ans)
        ans.append(root.val)
        if root.right:
            self._inorder_traversal(root.right, ans)
        return ans

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = []
        ans = []
        while stack or root:
            # 根节点及左子节点入栈
            while root:
                stack.append(root)
                root = root.left
            # 根节点及左子节点出栈
            root = stack.pop()
            ans.append(root.val)
            # 考虑右子结点
            root = root.right
        return ans
