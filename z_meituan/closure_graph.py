# encoding=utf-8

def min_edge_plus():
    line = input().split()
    n = int(line[0])
    m = int(line[1])
    g = [[0 for _ in range(n)] for _ in range(n)]
    d = [0 for _ in range(n)]
    for i in range(m):
        line = input().split()
        x = int(line[0])
        y = int(line[1])
        g[x - 1][y - 1] = 1
        d[x - 1] += 1
        d[y - 1] += 1

    dfs()
    ans = 0
    while True:
        mark = False
        for x in range(n - 1):
            for y in range(x + 1, n):
                if g[x][y] == 0 and d[x] + d[y] >= n:
                    g[x][y] = 1
                    d[x] += 1
                    d[y] += 1
                    ans += 1
                    mark = True
        print(ans)
        if not mark:
            return ans


def dfs():
    """"""


min_edge_plus()
