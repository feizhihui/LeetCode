# encoding=utf-8

char_ix = {chr(c): i + 1 for i, c in enumerate(range(97, 123))}


def decode(s):
    n = len(s)
    c = s[-1]
    k = char_ix[c] - n + 1
    return k + (54 - n) * (n - 1) // 2


n = int(input())
while n > 0:
    s = input()
    print(decode(s))
    n -= 1
