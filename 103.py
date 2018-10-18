'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right,
then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = [[root.val]]
        stack = [root]
        ii = 0
        while True:
            temp = []
            t = []
            for s in stack:
                if s.left:
                    temp.append(s.left.val)
                    t.append(s.left)
                if s.right:
                    temp.append(s.right.val)
                    t.append(s.right)
            if len(t) == 0:
                break
            stack = [t[i] for i in range(0,len(t))]
            if ii%2 == 0:
                res.append(temp[::-1])
            else:
                res.append(temp)
            ii += 1
        return res