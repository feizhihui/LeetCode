# encoding=utf-8

'''
3Sum:
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.
Note: The solution set must not contain duplicate triplets.
For example, given array S = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        m = len(nums)
        ans = []
        duplic = set()
        for i in range(m - 2):
            if i > 0 and nums[i] == nums[i - 1]: continue
            tupl = self.findTwoNums(nums[i + 1:], -nums[i])
            for (a, b) in tupl:
                if (a, b) not in duplic:
                    ans.append((nums[i], a, b))
                    duplic.add((a, b))
        return ans

    def findTwoNums(self, nums, target):
        left = 0
        right = len(nums) - 1
        ans = []
        while left < right:
            if nums[left] + nums[right] == target:
                ans.append((nums[left], nums[right]))
                right -= 1
                left += 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))
