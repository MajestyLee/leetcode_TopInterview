'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if not l1 or not l2:
            return l2 or l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2


#iterat
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        newList = dummy
        while (l1 and l2):
            if l1.val <= l2.val:
                newList.next = l1
                l1 = l1.next
                newList = newList.next

            else:
                newList.next = l2
                l2 = l2.next
                newList = newList.next

        if (l1):
            newList.next = l1
        elif (l2):
            newList.next = l2

        return dummy.next