# encoding=utf-8

'''
Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = dict()
        for i, e in enumerate(nums):
            if target - nums[i] in d:
                return [d[target - nums[i]], i]
            else:
                d[e] = i
        raise Exception


if __name__ == '__main__':
    s = Solution()
    k = s.twoSum([2, 3, 4], 6)
    print(k)
