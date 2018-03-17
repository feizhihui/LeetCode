# encoding=utf-8
class Solution:
    # def rotate(self, nums, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: void Do not return anything, modify nums in-place instead.
    #     """
    #     if k > len(nums):
    #         k = k - len(nums)
    #     s = nums[-k:] + nums[:-k]
    #
    #     for i, c in enumerate(s):
    #         nums[i] = s[i]

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        k = k % len(nums)
        reverse(nums, 0, len(nums) - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, len(nums) - 1)


if __name__ == '__main__':
    s = Solution()
    nums = list(range(1, 3))
    s.rotate(nums, 0)
    print(nums)
