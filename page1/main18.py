# encoding=utf-8

class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        res = []
        duplic = set()
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                ans = self.findTwoNums(nums[j + 1:], target - nums[i] - nums[j])
                for (a, b) in ans:
                    if (nums[i], nums[j], a) not in duplic:
                        res.append((nums[i], nums[j], a, b))
                        duplic.add((nums[i], nums[j], a))

        return res

    def findTwoNums(self, nums, target):
        left = 0
        right = len(nums) - 1
        ans = []
        while left < right:
            pnum = nums[left] + nums[right]
            if pnum == target:
                ans.append((nums[left], nums[right]))
                left += 1
                right -= 1
            elif pnum < target:
                left += 1
            else:
                right -= 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.fourSum([-3, -2, -1, 0, 0, 1, 2, 3], 0))
