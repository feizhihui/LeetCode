# encoding=utf-8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None
        p = q = head
        c1 = c2 = 0
        loop = 0
        while p.next and p.next.next and q.next:
            p = p.next.next
            q = q.next
            c1 += 2
            c2 += 1
            if p == q:
                loop = c1 - c2
                break
        if loop == 0:
            return None

        p = q = head
        while loop > 0:
            loop -= 1
            p = p.next
        while p != q:
            p = p.next
            q = q.next
        return p


if __name__ == '__main__':
    sl = Solution()
    head = ListNode(0)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    ans = sl.detectCycle(head)
    print(ans)
