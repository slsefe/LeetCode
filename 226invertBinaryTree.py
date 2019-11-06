"""
leetcode 226 翻转二叉树
递归法：翻转当前结点（根节点）的左右子树，交换左右子树，返回根节点。
非递归法：遍历二叉树所有节点（深度or广度），翻转所有节点的左右结点。这里使用基于队列的BFS。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invert_tree_v1(self, root: TreeNode) -> TreeNode:
        # 递归
        if not root:
            return None
        left = self.invert_tree_v1(root.left)
        right = self.invert_tree_v1(root.right)
        root.left, root.right = right, left
        return root

    def invert_tree_v2(self, root: TreeNode) -> TreeNode:
        # 非递归，层序遍历，基于队列
        if not root:
            return None
        q = [root]
        while q:
            node = q.pop(0)
            node.left, node.right = node.right, node.left
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return root
