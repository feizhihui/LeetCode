# encoding=utf-8
"""
1 2 3 4 5 6 7 8
15
"""

nlist = list(map(int, input().split()))
target = int(input())

low = 0
high = 1
ans = []
total = nlist[low] + nlist[high]

while low < high:
    if total == target:
        ans.append((low, high))
        if high + 1 >= len(nlist): break
        total += nlist[high + 1] - nlist[low]
        low += 1
        high += 1

    elif total < target:
        if high + 1 >= len(nlist): break
        total += nlist[high + 1]
        high += 1
    elif total > target:
        total -= nlist[low]
        low += 1

if len(ans) != 0:
    for (i, j) in ans:
        print(' '.join(map(str, (nlist[i:j + 1]))))
else:
    print(-1)
