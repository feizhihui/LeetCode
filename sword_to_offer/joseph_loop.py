# encoding=utf-8

def find(n, m):
    nums = list(range(n))
    b = [True] * n
    c = 0
    while n > 0:
        for i, num in enumerate(nums):
            if not b[i]:
                continue
            c += 1
            if c == m:
                b[i] = False
                c = 0
                n -= 1
                print(b)
                if n == 0:
                    return num

if __name__ == '__main__':
    ans = find(15, 13)
    print(ans)
