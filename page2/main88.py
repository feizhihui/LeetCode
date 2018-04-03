# encoding=utf-8

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        del nums1[m:]
        k = p = 0
        while p < n:
            while k < len(nums1) and nums1[k] < nums2[p]:
                k += 1
            nums1.insert(k, nums2[p])
            p += 1
            k += 1


if __name__ == '__main__':
    sl = Solution()
    a = [0]
    sl.merge(a, 0, [1], 1)
    print(a)
