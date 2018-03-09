# encoding=utf-8
"""
Search Insert Position:
Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.
"""


class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            p = (left + right) // 2
            if nums[p] == target:
                return p
            elif nums[p] < target:
                left = p + 1
            else:
                right = p - 1

        return left


'''
[1,3,5,6]
5
'''
if __name__ == '__main__':
    s = Solution()
    print(s.searchInsert([1, 3, 5, 6], 8))
