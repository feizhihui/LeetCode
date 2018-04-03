# encoding=utf-8

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import math


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        low, high = 0, len(nums) - 1
        mid = int(math.ceil((low + high) / 2))
        h = TreeNode(nums[mid])
        h.left = self.sortedArrayToBST(nums[low:mid])
        h.right = self.sortedArrayToBST(nums[mid + 1:])
        return h


if __name__ == '__main__':
    sl = Solution()
    ans = sl.sortedArrayToBST([-10, -3, 0, 5, 9])
