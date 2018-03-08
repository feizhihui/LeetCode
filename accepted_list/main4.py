# encoding=utf-8

'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        if m == 0:
            return (nums2[n // 2 - 1] + nums2[n // 2]) / 2 if n % 2 == 0 else nums2[n // 2]
        left = 0
        right = m - 1
        while True:
            p1 = (left + right) // 2
            p2 = (m + n) // 2 - p1 - 2

            L1 = nums1[p1] if p1 >= 0 else -(1 << 32)
            L2 = nums2[p2] if p2 >= 0 else -(1 << 32)
            R1 = nums1[p1 + 1] if p1 + 1 != m  else 1 << 32
            R2 = nums2[p2 + 1] if p2 + 1 != n  else 1 << 32

            if L1 > R2:  # p1 too large
                right = p1 - 1
            elif L2 > R1:  # p2 too large, p1 too small
                left = p1 + 1
            else:
                break
        if (m + n) % 2 == 0:
            return (max(L1, L2) + min(R1, R2)) / 2
        else:
            return min(R1, R2)


if __name__ == '__main__':
    s = Solution()
    h = s.findMedianSortedArrays([1, 3], [2])
    print(h)
