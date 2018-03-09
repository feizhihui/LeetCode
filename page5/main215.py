# encoding=utf-8

'''
Kth Largest Element in an Array:
Find the kth largest element in an unsorted array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
For example,
Given [3,2,1,5,6,4] and k = 2, return 5.
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
'''


class MaxHeap:
    def __init__(self, a):
        """
        :param a:  List[int]
        """
        self.a = a
        self.n = len(a)

        for i in reversed(range(self.n // 2)):
            self.sink(i)

    def sink(self, ix):
        """
        :param ix:
        :return:
        """
        lv = rv = -(1 << 31)
        if 2 * ix + 1 < self.n:
            lv = self.a[2 * ix + 1]
        if 2 * ix + 2 < self.n:
            rv = self.a[2 * ix + 2]
        if lv >= rv and lv > self.a[ix]:
            self.a[ix], self.a[2 * ix + 1] = self.a[2 * ix + 1], self.a[ix]
            self.sink(2 * ix + 1)
        elif rv >= lv and rv > self.a[ix]:
            self.a[ix], self.a[2 * ix + 2] = self.a[2 * ix + 2], self.a[ix]
            self.sink(2 * ix + 2)

    def swim(self, ix):
        """
        :param ix:
        :return:
        """
        if (ix - 1) // 2 >= 0 and self.a[(ix - 1) // 2] < self.a[ix]:
            self.a[ix], self.a[(ix - 1) // 2] = self.a[(ix - 1) // 2], self.a[ix]
            self.swim((ix - 1) // 2)

    def pop(self):
        """
        :return:
        """
        ret = self.a[0]
        self.n -= 1
        if self.n >= 1:
            self.a[0] = self.a.pop()
            self.sink(0)
        return ret

    def insert(self, v):
        """
        :param v:  int
        :return:
        """
        self.a.append(v)
        self.n += 1
        self.swim(self.n - 1)


class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        h = MaxHeap(nums)
        v = None
        while k != 0:
            v = h.pop()
            k -= 1
        return v


if __name__ == '__main__':
    s = Solution()
    v = s.findKthLargest([3, 2, 1, 5, 6, 4], 2)
    print(v)
    m = MaxHeap([3, 2, 1, 5, 6, 4])
    m.insert(3)
    m.pop()
    print(m.a)
