# encoding=utf-8
from copy import deepcopy

scan = raw_input().split()
n = int(scan[0])
m = int(scan[1])

scan = raw_input().split()
x = int(scan[0])
y = int(scan[1])

a = [[0 for i in range(m)] for j in range(n)]
hashMap = deepcopy(a)

for i in range(n):
    scan = raw_input().split()
    for j in range(m):
        a[i][j] = int(scan[j])

max_value = 0


def dfs(x, y):
    global max_value, a, hashMap
    if hashMap[x][y] > 0:
        return
    if a[x][y] > max_value:
        max_value = a[x][y]
    hashMap[x][y] = 1
    if x + 1 < n and a[x][y] <= a[x + 1][y]:
        dfs(x + 1, y)
    if x - 1 >= 0 and a[x][y] <= a[x - 1][y]:
        dfs(x - 1, y)
    if y + 1 < m and a[x][y] <= a[x][y + 1]:
        dfs(x, y + 1)
    if y - 1 >= 0 and a[x][y] <= a[x][y - 1]:
        dfs(x, y - 1)


dfs(x - 1, y - 1)
print max_value

"""
2 2
1 1
2 1
1 3
"""
