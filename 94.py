'''
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#iterate
class Solution:

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        t, stack = [], []
        while root or len(stack) > 0:

            while root:
                stack.append(root)
                root = root.left

            t.append(stack[-1].val)
            root = stack[-1].right
            del stack[-1]

        return t

    def inorderTraversal2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        re = []

        def inOrder(root):
            if root:
                inOrder(root.left)
                re.append(root.val)
                inOrder(root.right)
        inOrder(root)
        return re