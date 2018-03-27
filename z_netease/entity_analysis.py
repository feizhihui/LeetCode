# encoding=utf-8
from collections import defaultdict


def str_to_list(s):
    ans = []
    start = 0
    for i, c in enumerate(s):
        if c in ['{', ',', '}']:
            if i > start:
                ans.append(s[start:i])
            ans.append(c)
            start = i + 1
    return ans


def analysis(alist):
    ad = defaultdict(set)
    prio = 1
    for a in alist:
        if a == '{':
            prio += 1
        elif a == '}':
            prio -= 1
        elif a == ',':
            continue
        else:
            ad[a].add(prio)
    return ad


if __name__ == '__main__':
    s = input()
    ans = str_to_list(s)
    kvs = analysis(ans)
    while True:
        key = input()
        print(list(kvs[key]))
