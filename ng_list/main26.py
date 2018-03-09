# encoding=utf-8

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        p = 0
        while p < len(nums) - 1:
            if nums[p] != nums[p + 1]:
                p += 1
            else:
                del nums[p + 1]
        return len(nums)


if __name__ == '__main__':
    s = Solution()
    nums = s.removeDuplicates([0, 0, 0, 0, 0])
    print(nums)
