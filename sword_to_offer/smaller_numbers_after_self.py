# encoding=utf-8

class Solution:
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print(nums)
        self.c = 0
        res = self.divide_and_conquer(nums, 0, len(nums) - 1)
        print(res)

    def divide_and_conquer(self, nums, left, right):
        if left == right:
            return [nums[left]]
        middle = (left + right) // 2
        nums1 = self.divide_and_conquer(nums, left, middle)
        nums2 = self.divide_and_conquer(nums, middle + 1, right)
        i = j = 0
        res = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                self.c += len(nums1[i:])
                res.append(nums2[j])
                j += 1
        res += nums1[i:]
        res += nums2[j:]
        return res


if __name__ == '__main__':
    sl = Solution()
    sl.countSmaller([1, 3, 2, 3, 1])
    print(sl.c)
