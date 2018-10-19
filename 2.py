'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        dummyNode = ListNode(-1)
        cur = dummyNode
        op = 0
        f = True
        while l1 and l2:
            m = l1.val + l2.val + op
            if m >= 10:
                cur.next = ListNode(m % 10)
                op = int(m / 10)
            else:
                cur.next = ListNode(m)
                op = 0
            l1 = l1.next
            l2 = l2.next
            cur = cur.next

        if l1:
            while l1:
                m = l1.val + op
                if m >= 10:
                    cur.next = ListNode(m % 10)
                    op = int(m / 10)
                else:
                    cur.next = ListNode(m)
                    op = 0
                l1 = l1.next
                cur = cur.next
        if l2:
            while l2:
                m = l2.val + op
                if m >= 10:
                    cur.next = ListNode(m % 10)
                    op = int(m / 10)
                else:
                    cur.next = ListNode(m)
                    op = 0
                l2 = l2.next
                cur = cur.next
        if op > 0:
            cur.next = ListNode(op)
        return dummyNode.next