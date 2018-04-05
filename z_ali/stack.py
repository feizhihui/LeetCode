# encoding=utf-8

def adjustDown(A, k, len):
    A[0] = A[k]
    i = 2 * k
    while (i <= len):
        if i < len and A[i] < A[i + 1]: i += 1
        if A[0] > A[i]:
            break
        else:
            A[k] = A[i]
            A[i] = A[0]
            k = i
        i *= 2


def buildMaxHeap(A, len):
    i = len // 2
    while i > 0:
        adjustDown(A, i, len)
        i -= 1


def heapSort(A, len):
    buildMaxHeap(A, len)
    for i in range(len, 1, -1):
        A[1], A[i] = A[i], A[1]
        adjustDown(A, 1, i - 1)
    return A[1:]


k = 3
A = [5, 2, 1, 6]
A.insert(0, 0)
print(A)
print(heapSort(A, len(A) - 1)[:k])

if __name__ == '__main__':
    pass
