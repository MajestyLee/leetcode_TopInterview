'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

'''
# recurve to find the max depth
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = 0
        if (root):
            lchilddeep = self.maxDepth(root.left)
            rchilddeep = self.maxDepth(root.right)
            if lchilddeep >= rchilddeep:
                depth = lchilddeep+1
            else:
                depth = rchilddeep+1
        return depth