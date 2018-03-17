# encoding=utf-8

class Solution:
    # def search(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: int
    #     """
    #     low, high = 0, len(nums) - 1
    #     while low < high:
    #         mid = (low + high) // 2
    #         if nums[mid] == target:
    #             return mid
    #         if nums[mid] > nums[high]:  # minimus on the right
    #             if target > nums[mid]:  # target on the right
    #                 low = mid
    #             else:  # target on the right
    #                 high = mid - 1
    #         else:  # minimus on the left
    #             if target < nums[mid]:
    #                 high = mid - 1
    #             else:
    #                 if target > nums[high]:
    #                     high = mid - 1
    #                 else:
    #                     low = mid
    #     return -1

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return -1

        def bi_search(nums, low, high, target):
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    low = mid + 1
                elif nums[mid] > target:
                    high = mid - 1
            return -1

        low, high = 0, n - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid

        if target > nums[n - 1]:
            return bi_search(nums, 0, low - 1, target)
        else:
            return bi_search(nums, low, n - 1, target)


if __name__ == '__main__':
    s = Solution()
    ans = s.search([1], 0)
    print(ans)
