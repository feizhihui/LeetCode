# encoding=utf-8

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


import math


class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # n = 0
        # p = head
        # while p:
        #     p = p.next
        #     n += 1
        # h = math.ceil(n / 2)
        # p = q = head
        # while h > 0:
        #     p = p.next
        #     h -= 1
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        p = self.reverse(slow)
        q = head
        while p:
            if p.val != q.val:
                return False
            p = p.next
            q = q.next
        return True

    def reverse(self, head):
        if not head:
            return None
        h = head
        p = head.next
        while p:
            temp = p.next
            p.next = h
            h = p
            p = temp
        head.next = None
        return h


if __name__ == '__main__':
    sl = Solution()

    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(1)
    # n4 = ListNode(1)
    n1.next = n2
    n2.next = n3
    # n3.next = n4
    a = sl.isPalindrome(n1)
    print(a)
