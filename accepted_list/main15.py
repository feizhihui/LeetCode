# encoding=utf-8


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
            for j in range(i + 1, m - 1):
                if (nums[i], nums[j]) in duplic:
                    continue
                if self.canFindNum(nums[j + 1:], -nums[i] - nums[j]):
                    ans.append((nums[i], nums[j], -nums[i] - nums[j]))
                    duplic.add((nums[i], nums[j]))

        return ans

    def canFindNum(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            p = (left + right) // 2
            if nums[p] == target:
                return True
            elif nums[p] < target:
                left = p + 1
            else:
                right = p - 1
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))
