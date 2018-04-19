# encoding=utf-8

import sys

scan = sys.stdin

N = int(scan.readline())
while N > 0:
    N -= 1
    k = int(scan.readline())
    count = 1
    while k % 2 == 0:
        k //= 2
        count *= 2
    if k % 2 != 0 and count % 2 == 0:
        print(k, count)
    else:
        print('No')
