# encoding=utf-8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p = headA
        c1 = 0
        while p:
            p = p.next
            c1 += 1
        p = headB
        c2 = 0
        while p:
            p = p.next
            c2 += 1
        if c1 < c2:
            c1, c2 = c2, c1
            p, q = headB, headA
        else:
            p, q = headA, headB

        while c1 > c2:
            c1 -= 1
            p = p.next

        while p != None:
            if p == q:
                return p
            else:
                p = p.next
                q = q.next


if __name__ == '__main__':
    pass
