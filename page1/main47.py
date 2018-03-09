# encoding=utf-8
'''
Permutation:
Given a collection of numbers that might contain duplicates, return all possible unique permutations.
For example,
[1,1,2] have the following unique permutations:
'''
from copy import deepcopy


class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.nums = nums
        self.n = len(nums)
        self.ans = []
        occur = [0 for num in nums]
        self.dfs(occur, [])
        return list(set(self.ans))

    def dfs(self, occur, result):
        if len(result) == self.n:
            self.ans.append(tuple(result))
            return

        for i, num in enumerate(self.nums):
            if occur[i] == 0:
                result.append(num)
                occur[i] = 1
                self.dfs(occur, result)
                occur[i] = 0
                result.pop()


if __name__ == '__main__':
    s = Solution()
    ans = s.permuteUnique([1, 1, 2])
    print(ans)
