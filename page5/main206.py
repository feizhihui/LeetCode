# encoding=utf-8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        if not head:
            return None
        h = head
        p = head.next
        while p:
            p_next = p.next
            p.next = h
            h = p
            p = p_next
        head.next = None
        return h


if __name__ == '__main__':
    pass
