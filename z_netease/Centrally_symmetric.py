# encoding=utf-8

import sys

scan = sys.stdin
T = int(scan.readline().strip())
ans = []
while T > 0:
    T -= 1
    line = scan.readline().split()
    N, M = int(line[0]), int(line[1])
    h = 1
    while h * N < M:
        h += 2
    g = []
    for i in range(N):
        line = list(scan.readline().strip())
        g.append(line * h)
    g = g * h
    w = len(g[0])
    x = (w - M) // 2
    res = []
    for i in range(M):
        res.append(''.join(g[x + i][x:x + M]))
    ans.append(res)
    scan.readline()

for a in ans:
    for line in a:
        print(line)
    print()

"""
3 
3 5
abc
bcd
efg
"""
