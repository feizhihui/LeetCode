# encoding=utf-8


class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        p = 0
        while p < len(nums):
            if nums[p] == val:
                del nums[p]
            else:
                p += 1
        return len(nums)
