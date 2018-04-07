# encoding=utf-8

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        pool = set()
        for n in nums:
            if n in pool:
                return True
            else:
                pool.add(n)
        return False


if __name__ == '__main__':
    pass
