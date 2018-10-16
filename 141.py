'''
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head==None or head.next==None:
            return False
        else:
            low = head.next
            fast = head.next.next
            while fast:
                if fast == low:
                    return True
                if fast.next == None or fast.next.next == None:
                    return False
                fast = fast.next.next
                low = low.next
            return False