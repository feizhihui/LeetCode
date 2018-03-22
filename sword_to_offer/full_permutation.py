# encoding=utf-8

ans = []


def permutation(clist, ix=0):
    if ix == len(clist) - 1:
        ret = ''.join(clist)
        ans.append(ret)
        print(ret)
        return
    permutation(clist, ix + 1)
    for i in range(ix + 1, len(clist)):
        clist[ix], clist[i] = clist[i], clist[ix]
        permutation(clist, ix + 1)
        clist[ix], clist[i] = clist[i], clist[ix]


if __name__ == '__main__':
    clist = list(input())
    permutation(clist)
    print(len(ans))
