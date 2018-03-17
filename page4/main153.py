# encoding=utf-8
class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low, high = 0, len(nums) - 1
        while low < high:
            pivot = (low + high) // 2
            if nums[pivot] > nums[high]:
                low = pivot + 1
            else:
                high = pivot
        return nums[low]


if __name__ == '__main__':
    s = Solution()
    ans = s.findMin([5, 1, 2, 3, 4])
    print(ans)
