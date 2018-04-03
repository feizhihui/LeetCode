# encoding=utf-8

# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return
        p = head
        while p.next != None:
            p_next = p.next
            if p_next.val == p.val:
                p.next = p_next.next
            else:
                p = p.next

        return head


if __name__ == '__main__':
    head = ListNode(1)
    # head = None

    sl = Solution()
    head = sl.deleteDuplicates(head)
    while head != None:
        print(head.val)
        head = head.next
