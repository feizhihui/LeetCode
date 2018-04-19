# encoding=utf-8


import sys

scan = sys.stdin
count = 0


def dfs(ans, nums):
    global count
    if not nums:
        if ans and ans == ans[::-1]:
            count += 1
        return
    c = nums[0]
    ans.append(c)
    dfs(ans, nums[1:])
    del ans[-1]
    dfs(ans, nums[1:])


s = scan.readline().strip()
n = len(s)

dfs([], s)

print(count)
