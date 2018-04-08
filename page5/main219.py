# encoding=utf-8
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hashTable = dict()
        for i in range(len(nums)):
            if i > k:
                hashTable[nums[i - k - 1]] = 0
            if nums[i] not in hashTable or hashTable[nums[i]] == 0:
                hashTable[nums[i]] = 1
            else:
                return True
        return False


if __name__ == '__main__':
    sl = Solution()
    a = sl.containsNearbyDuplicate([1, 2, 4, 5, 6], 4)
    print(a)
