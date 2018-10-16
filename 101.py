'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isValid(lf,lr):
            if not lf and not lr:
                return True
            elif not lf or not lr:
                return False
            if lf.val == lr.val:
                return isValid(lf.left,lr.right) and isValid(lf.right,lr.left)
            else:
                return False
        if root:
            return isValid(root.left,root.right)
        else:
            return True

#BFS
from collections import deque

class Solution:
    def isSymmetric(self, root):
        if not root: return True
        if not root.left and not root.right:
            return True
        if not root.left or not root.right:
            return False
        queue = deque([root.left,root.right])
        while queue:
            node1 = queue.popleft()
            node2 = queue.popleft()
            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            queue.append(node1.left)
            queue.append(node2.right)
            queue.append(node1.right)
            queue.append(node2.left)
        return True