# encoding=utf-8

'''
Merge Two Sorted Lists:
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.
Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = l = ListNode(None)
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                l.next = ListNode(l1.val)
                l = l.next
                l1 = l1.next
            else:
                l.next = ListNode(l2.val)
                l = l.next
                l2 = l2.next

        if l1 != None:
            l.next = l1
        elif l2 != None:
            l.next = l2
        return head.next


def print_list(l):
    while l != None:
        print(l.val, end='')
        l = l.next
        if l != None:
            print(end='->')
    print()


if __name__ == '__main__':
    list1 = [1, 2, 3]
    list2 = [1, 3, 4]
    head1 = l1 = ListNode(None)
    head2 = l2 = ListNode(None)

    for c in list1:
        l1.next = ListNode(c)
        l1 = l1.next
    for c in list2:
        l2.next = ListNode(c)
        l2 = l2.next

    print_list(head1.next)
    print_list(head2.next)
    s = Solution()
    head3 = s.mergeTwoLists(head1.next, head2.next)
    print_list(head3)
