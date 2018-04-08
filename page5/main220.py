# encoding=utf-8

"""
Given an array of integers, find out whether there are two distinct indices i and j in the array
such that the absolute difference between nums[i] and nums[j] is at most t
and the absolute difference between i and j is at most k.
"""


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if not nums or k <= 0 or t < 0:
            return False
        numsDict = dict()
        for i in range(len(nums)):
            if i > k:
                numsDict.pop((nums[i - k - 1]) // (t + 1))

            bucket = nums[i] // (t + 1)
            for j in [bucket - 1, bucket, bucket + 1]:  # symmetric
                if j in numsDict and abs(numsDict[j] - nums[i]) <= t:
                    return True
            numsDict[bucket] = nums[i]
        return False


if __name__ == '__main__':
    sl = Solution()
    a = sl.containsNearbyAlmostDuplicate([-3, 3], 2, 4)
    print(a)
