# encoding=utf-8

import sys

scan = sys.stdin


N = int(scan.readline())
while N > 0:
    N -= 1
    k = int(scan.readline())
    find = False
    for i in range(1, k // 3):
        i = i * 2
        if k % i == 0 and k // i % 2 != 0:
            find = True
            break
    if find:
        print(k // i, i)
    else:
        print('No')



"""
#coding=utf-8
import sys 
for line in sys.stdin:
    a = line.split()
    print(int(a[0]) + int(a[1]))
"""
