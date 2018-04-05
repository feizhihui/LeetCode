# encoding=utf-8

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        key, value = None, 0
        for n in nums:
            if n != key:
                if value == 0:
                    key = n
                    value = 1
                else:
                    value -= 1
            else:
                value += 1
        return key


if __name__ == '__main__':
    pass
