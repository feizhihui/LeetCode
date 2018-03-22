# encoding=utf-8

def find(alist):
    k, count = None, 1
    for a in alist:
        if k == a:
            count += 1
        elif k != a:
            count -= 1
        if count == 0:
            k = a
            count = 1
    return k


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
    ans = find([1, 3, 1, 3, 2, 3])
    print(ans)
    ans = findK([1, 3, 1, 3, 2, 3], 6 // 2)
    print(ans)
