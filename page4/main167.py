# encoding=utf-8

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        low, high = 0, len(numbers) - 1
        while low < high:
            if numbers[low] + numbers[high] > target:
                high -= 1
            elif numbers[low] + numbers[high] < target:
                low += 1
            else:
                return (low + 1, high + 1)


if __name__ == '__main__':
    pass
