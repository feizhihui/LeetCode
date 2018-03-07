# encoding=utf-8
'''
Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def creat_list(l):
    header = p = ListNode(l[0])
    for e in l[1:]:
        p.next = ListNode(e)
        p = p.next
    return header


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = self.list2int(l1)
        num2 = self.list2int(l2)
        return self.int2list(num1 + num2)

    def list2int(self, l):
        sum = l.val
        r = 10
        while l.next:
            l = l.next
            sum += r * l.val
            r *= 10
        return sum

    def int2list(self, num):
        head = l = ListNode(num % 10)
        num //= 10
        while num != 0:
            l.next = ListNode(num % 10)
            l = l.next
            num //= 10
        return head


if __name__ == '__main__':
    s = Solution()
    l1 = creat_list([2, 4, 3])
    l2 = creat_list([5, 6, 4])
    k = s.addTwoNumbers(l1, l2)
