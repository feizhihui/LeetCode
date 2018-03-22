# encoding=utf-8

import numpy as np

arr = list(np.random.randint(0, 100, [20]))


def select_sort(lists):
    """选择排序"""
    count = len(lists)
    for i in range(0, count):
        min = i
        for j in range(i + 1, count):
            if lists[min] > lists[j]:
                min = j
        lists[i], lists[min] = lists[min], lists[i]
    return lists


def bubble_sort(lists):
    """冒泡排序"""
    count = len(lists)
    for i in range(0, count):
        for j in range(0, count - i - 1):
            if lists[j] > lists[j + 1]:
                lists[j], lists[j + 1] = lists[j + 1], lists[j]
    return lists


def merge_sort(lists):
    """归并排序"""
    if len(lists) <= 1:
        return lists
    num = len(lists) // 2
    left = merge_sort(lists[:num])
    right = merge_sort(lists[num:])

    def merge(l, r):
        i, j = 0, 0
        res = []
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                res.append(l[i])
                i += 1
            else:
                res.append(r[j])
                j += 1
        res += l[i:]
        res += r[j:]
        return res

    return merge(left, right)


def quick_sort(lists, left, right):
    if left >= right:
        return
    low, high = left, right
    key = lists[left]
    while left < right:
        while left < right and key <= lists[right]:
            right -= 1
        lists[left] = lists[right]
        while left < right and key >= lists[left]:
            left += 1
        lists[right] = lists[left]
    print(left, right)
    assert left == right
    lists[right] = key
    quick_sort(lists, low, left - 1)
    quick_sort(lists, left + 1, high)  # print(select_sort(arr))
    return lists



print(arr)
# print(bubble_sort(arr))
# print(merge_sort(arr))
print(quick_sort(arr, 0, len(arr) - 1))

