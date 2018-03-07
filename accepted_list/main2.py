# encoding=utf-8


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
        return int(''.join(map(str, l))[::-1])

    def int2list(self, l):
        return list(map(int, list(str(l)[::-1])))


if __name__ == '__main__':
    s = Solution()
    k = s.addTwoNumbers([2, 4, 3], [5, 6, 4])
    print(k)
