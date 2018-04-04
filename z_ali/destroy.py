# encoding=utf-8

def main():
    n = int(raw_input())
    m = int(raw_input())
    g = []
    for i in range(n):
        line = raw_input().split()
        cols = []
        for j in range(m):
            cols.append(int(line[j]))
        g.append(cols)
    best = 0
    for i in range(n):
        for j in range(m):
            if g[i][j] == 1:
                ans = count(g, i, j)
                if ans > best:
                    best = ans

    for i in range(n):
        for j in range(m):
            if g[i][j] == 1:
                ans = count(g, i, j)
                if ans == best:
                    print i, j


def count(g, x, y):
    n = len(g)
    m = len(g[0])
    num = 0
    i = x - 1
    while i >= 0:
        if g[i][y] == 1:
            num += 1
            i -= 1
        else:
            break
    i = x + 1
    while i < n:
        if g[i][y] == 1:
            num += 1
            i += 1
        else:
            break
    j = y - 1
    while j >= 0:
        if g[x][j] == 1:
            num += 1
            j -= 1
        else:
            break
    j = y + 1
    while j < m:
        if g[x][j] == 1:
            num += 1
            j += 1
        else:
            break
    return num + 1


if __name__ == '__main__':
    main()

"""
3
3
1 1 1
0 0 0
1 1 1

4
5
1 0 1 0 1
1 0 1 0 0
0 1 1 1 1
1 1 1 1 0

"""
