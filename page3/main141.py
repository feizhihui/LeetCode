# encoding=utf-8

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
        if not head: return False
        p = q = head
        while p.next and p.next.next and q.next:
            p = p.next.next
            q = q.next
            if p == q:
                return True
        return False


if __name__ == '__main__':
    pass
