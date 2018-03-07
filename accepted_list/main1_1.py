# encoding=utf-8

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
