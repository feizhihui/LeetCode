# encoding=utf-8

'''
Permutations:
Given a collection of distinct numbers, return all possible permutations.
'''

from copy import deepcopy


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.nums = nums
        self.n = len(nums)
        self.ans = []
        occur = {num: 0 for num in nums}
        self.dfs(occur, [])
        return self.ans

    def dfs(self, occur, result):
        if len(result) == self.n:
            self.ans.append(deepcopy(result))
            return

        for num in self.nums:
            if occur[num] == 0:
                result.append(num)
                occur[num] = 1
                self.dfs(occur, result)
                occur[num] = 0
                result.pop()


if __name__ == '__main__':
    s = Solution()
    ans = s.permute([1, 2, 3])
    print(ans)
