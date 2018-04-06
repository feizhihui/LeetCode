# encoding=utf-8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head and head.val == val:
            head = head.next
        if not head:
            return None
        p = head
        while p and p.next:
            q = p.next
            if q.val == val:
                p.next = q.next
            else:
                p = p.next
        return head


if __name__ == '__main__':
    pass
