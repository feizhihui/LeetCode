# encoding=utf-8
'''
3Sum Closest:
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.
    For example, given array S = {-1 2 1 -4}, and target = 1.
    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''


class Solution:
    def threeSumClosest(self, num, target):
        num.sort()
        result = num[0] + num[1] + num[2]
        for i in range(len(num) - 2):
            left, right = i + 1, len(num) - 1
            while left < right:
                sum = num[i] + num[left] + num[right]
                if sum == target:
                    return sum

                if abs(sum - target) < abs(result - target):
                    result = sum

                if sum < target:
                    left += 1
                elif sum > target:
                    right -= 1

        return result


if __name__ == '__main__':
    pass
