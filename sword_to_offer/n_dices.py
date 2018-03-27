# encoding=utf-8

max_value = 6


def n_dice(n, s):
    """sword to offer No.43"""
    # a[n][s]
    a = [[0 for j in range(s + 1)] for i in range(2)]
    a[0][0] = 1
    print(a)
    for i in range(1, n + 1):
        for j in range(1, s + 1):
            a[1][j] = sum([a[0][j - k] for k in range(1, max_value + 1) if j >= k])
        for j in range(1, s + 1):
            a[0][j] = a[1][j]
    print(a[1][s])


def n_dice_dp(n, s):
    """sword to offer No.43"""
    # a[n][s]
    a = [[0 for j in range(s + 1)] for i in range(n + 1)]
    a[0][0] = 1
    print(a)
    for i in range(1, n + 1):
        for j in range(1, s + 1):
            a[i][j] = sum([a[i - 1][j - k] for k in range(1, max_value + 1) if j >= k])
    print(a[n][s])


if __name__ == '__main__':
    n_dice_dp(102, 103)
