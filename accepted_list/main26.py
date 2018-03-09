# encoding=utf-8

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        i, j = 0, 1
        diff = 0
        while j < len(nums):
            if nums[i] != nums[j]:
                i = j
                diff += 1
            j += 1
        return diff + 1


if __name__ == '__main__':
    s = Solution()
    nums = s.removeDuplicates([0, 1, 1, 2, 2])
    print(nums)
