# encoding=utf-8


class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [1]  # append TC average O(1)
        i2 = i3 = i5 = 0
        while len(nums) < n:
            new_ugly = min(2 * nums[i2], 3 * nums[i3], 5 * nums[i5])
            if new_ugly == 2 * nums[i2]:
                i2 += 1
            if new_ugly == 3 * nums[i3]:
                i3 += 1
            if new_ugly == 5 * nums[i5]:
                i5 += 1
            nums.append(new_ugly)
        return nums[-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.nthUglyNumber(460))
