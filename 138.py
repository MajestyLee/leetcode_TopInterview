'''
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
BY USING DICTIONARY(hashmap) TO store nodes
'''

# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        d = {}
        if head:
            copy = RandomListNode(head.label)
        else:
            return None
        p = copy
        root = head
        while head:
            if head.next:
                p.next = RandomListNode(head.next.label)
            d[head] = p
            head = head.next
            p = p.next
        p = copy
        head = root
        while p:
            if head.random:
                p.random = d[head.random]
            p = p.next
            head = head.next
        return copy