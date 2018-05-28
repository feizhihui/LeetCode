class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.partition(nums, 0, len(nums) - 1, k - 1)

    def partition(self, nums, left, right, target):
        low, high = left, right
        pivot = nums[low]
        while low < high:
            while low < high and nums[high] <= pivot:
                high -= 1
            nums[low] = nums[high]
            while low < high and nums[low] >= pivot:
                low += 1
            nums[high] = nums[low]
        assert low == high
        p = low
        nums[p] = pivot
        if p > target:
            return self.partition(nums, left, p - 1, target)
        elif p < target:
            return self.partition(nums, p + 1, right, target)
        else:
            return nums[p]


if __name__ == '__main__':
    sl = Solution()
    nums = [5, 3, 4, 1, 2, 8, 7, 9, 6]
    a = sl.findKthLargest(nums, 5)
    print(a)
