# encoding=utf-8

"""
Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

You need to return the number of important reverse pairs in the given array.
"""


class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.ge = 1  # updating the count_ge of the previous nodes


def insert(root, x):
    if root is None:
        return Node(x)
    if x < root.val:
        root.left = insert(root.left, x)  # update left
    elif x > root.val:
        root.ge += 1
        root.right = insert(root.right, x)  # update right
    else:
        root.ge += 1
    return root


def search(root, x):
    count = 0
    while root != None:
        if x <= root.val:
            count += root.ge
            root = root.left
        elif x > root.val:
            root = root.right
    return count


class Solution:
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        head = None
        count = 0
        for i, x in enumerate(nums):
            t = search(head, 2 * x + 1)
            # print(t)
            count += t
            head = insert(head, x)
        return count


if __name__ == '__main__':
    sl = Solution()
    nums = list(range(50000))

    print(nums)
    ans = sl.reversePairs(nums)
    print(ans)
