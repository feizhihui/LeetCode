# encoding=utf-8
import numpy as np


def findK(alist, k):
    def partition(alist, start, end):
        pivot = alist[start]
        while start < end:
            while start < end and pivot <= alist[end]:
                end -= 1
            alist[start] = alist[end]
            while start < end and pivot >= alist[start]:
                start += 1
            alist[end] = alist[start]
        alist[start] = pivot
        return start

    n = len(alist)
    low, high = 0, n - 1
    p = partition(alist, 0, n - 1)
    while p != k:
        if p < k:
            low = p + 1
        if p > k:
            high = p - 1
        p = partition(alist, low, high)
    return alist[p]


if __name__ == '__main__':
    arr = list(np.random.randint(0, 100, [20]))
    print(arr)
    ans = findK(arr, 5)
    print(arr[:5])
