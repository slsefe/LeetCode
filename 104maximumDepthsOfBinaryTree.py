"""
leetcode 104 二叉树的最大深度
思路：递归解法。二叉树的最大深度=根节点的深度=1+max（左子树的最大深度，右子树的最大深度）
非递归：广度优先搜索，两个队列，类似于层次遍历
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def max_depth_v1(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1+max(self.max_depth_v1(root.left), self.max_depth_v1(root.right))

    def max_depth_v2(self, root: TreeNode) -> int:
        if not root:
            return 0
        depth = 0
        q = [root]
        next = []
        while q or next:
            depth += 1
            for node in q:
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            q = next
            next = []
        return depth
